#!/bin/bash
# Cron wrapper for night-feeds digest pipeline.
#
# Self-contained — does NOT rely on ~/.bashrc (which early-returns for
# non-interactive shells, so any exports there are invisible to cron).
#
# Cookies for Twitter CLI live in ./.env in cookie-string format:
#   auth_token=<hex>; ct0=<hex>
#
# Status of last run is written to ./.last-run-status — `cat` it to see
# whether the last cron run succeeded.

cd /home/calcifer/git/nigth-feeds || exit 1

LOG=/tmp/night-feeds.log
STATUS=/home/calcifer/git/nigth-feeds/.last-run-status
ENV_FILE=/home/calcifer/git/nigth-feeds/.env
CLAUDE=/home/calcifer/.local/bin/claude
TWITTER=/home/calcifer/.local/bin/twitter
DATE=$(date "+%Y-%m-%d %H:%M:%S")
TODAY=$(date "+%d-%m-%Y")

echo "=== digest run: $DATE ===" >> "$LOG"

fail() {
  local reason="$1"
  echo "[$DATE] FAIL: $reason" >> "$LOG"
  printf '%s  FAIL  %s\n' "$DATE" "$reason" > "$STATUS"
  exit 1
}

# ---- 1. Load Twitter cookies from .env ------------------------------------
if [ ! -r "$ENV_FILE" ]; then
  fail ".env не найден или нечитаем: $ENV_FILE"
fi

TWITTER_AUTH_TOKEN=$(grep -oE 'auth_token=[^;[:space:]]+' "$ENV_FILE" | head -1 | cut -d= -f2-)
TWITTER_CT0=$(grep -oE 'ct0=[^;[:space:]]+' "$ENV_FILE" | head -1 | cut -d= -f2-)

if [ -z "$TWITTER_AUTH_TOKEN" ] || [ -z "$TWITTER_CT0" ]; then
  fail ".env не содержит auth_token или ct0"
fi

export TWITTER_AUTH_TOKEN TWITTER_CT0

# ---- 2. Pre-flight: Twitter cookies actually work -------------------------
# One real API call. Cheap (1 request) and catches stale cookies BEFORE we
# burn a Claude session on broken auth.
if ! "$TWITTER" user-posts anthropicai --max 1 --json >/dev/null 2>>"$LOG"; then
  fail "twitter CLI вернул ошибку — куки в .env протухли, обнови их"
fi

# ---- 3. Pre-flight: claude binary alive -----------------------------------
if ! "$CLAUDE" --version >> "$LOG" 2>&1; then
  fail "claude --version упал — бинарь сломан или не в PATH"
fi

# ---- 4. Run the pipeline --------------------------------------------------
"$CLAUDE" --dangerously-skip-permissions -p "запусти пайплайн дайджеста" >> "$LOG" 2>&1
EXIT_CODE=$?

# ---- 5. Post-flight: Claude OAuth expiry detection ------------------------
if tail -100 "$LOG" | grep -q "OAuth token has expired\|authentication_error"; then
  fail "Claude OAuth протух — выполни 'claude /login' на машине"
fi

if [ $EXIT_CODE -ne 0 ]; then
  fail "claude завершился с кодом $EXIT_CODE"
fi

# ---- 6. Post-flight: digest actually produced -----------------------------
# Pipeline always creates digests/digest-DD-MM-YYYY.md, even on a fully quiet
# day. Its absence means claude exited 0 but didn't do the work.
if [ ! -f "digests/digest-${TODAY}.md" ]; then
  fail "claude отработал, но digests/digest-${TODAY}.md не появился"
fi

echo "[$DATE] OK" >> "$LOG"
printf '%s  OK    digest-%s.md\n' "$DATE" "$TODAY" > "$STATUS"
