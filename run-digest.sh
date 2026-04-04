#!/bin/bash
source /home/calcifer/.bashrc 2>/dev/null || true
cd /home/calcifer/git/nigth-feeds

LOG=/tmp/night-feeds.log
DATE=$(date "+%Y-%m-%d %H:%M:%S")

echo "=== digest run: $DATE ===" >> "$LOG"

# Проверка авторизации
if ! /home/calcifer/.local/bin/claude --version >> "$LOG" 2>&1; then
  echo "[$DATE] ОШИБКА: claude не запускается (возможно, разлогинен)" >> "$LOG"
  exit 1
fi

/home/calcifer/.local/bin/claude --dangerously-skip-permissions -p "запусти пайплайн дайджеста" >> "$LOG" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -ne 0 ]; then
  echo "[$DATE] ОШИБКА: claude завершился с кодом $EXIT_CODE" >> "$LOG"
else
  echo "[$DATE] OK" >> "$LOG"
fi
