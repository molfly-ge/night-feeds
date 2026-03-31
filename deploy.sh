#!/bin/bash
set -e
cd /home/calcifer/git/nigth-feeds/
git pull
rsync -av --delete site/ /var/www/rss.molfly.me/
