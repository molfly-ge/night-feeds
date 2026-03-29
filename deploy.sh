#!/bin/bash
cd /home/calcifer/git/night-feeds/
git pull
rsync -av --delete site/ /var/www/rss.molfly.me/
