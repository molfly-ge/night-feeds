#!/bin/bash
cd /home/calcifer/git/nigth-feeds
/home/calcifer/.local/bin/claude --dangerously-skip-permissions -p "запусти пайплайн дайджеста" >> /tmp/night-feeds.log 2>&1
