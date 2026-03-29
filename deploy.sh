#!/bin/bash
cd /home/calcifer/git/nigth-feeds/
git pull
python3 build/build.py
rsync -av --delete site/ /var/www/rss.molfly.me/
