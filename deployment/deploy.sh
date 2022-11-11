#!/bin/bash
git clone https://github.com/karthicksakkaravarti/FR.git /home/jenkins/wrh-bot
cd /home/jenkins/wrh-bot
git checkout main
mkdir -p media

sudo cp -rf ../nginx.conf  /etc/nginx/nginx.conf
sudo cp -rf ../default.conf  /etc/nginx/sites-available/default
cp ../.env /home/jenkins/wrh-bot/wrh_bot/
pip install uwsgi
python manage.py collectstatic

# Restart nginx
sudo /etc/init.d/nginx start || sudo /etc/init.d/nginx start

# Running Celery
#celery -A zp_result worker -l info &
#celery -A zp_result beat &
#nohup python manage.py zwift_bot &
#python manage.py whois_bot_start &
# Running Server
uwsgi --socket mysite.sock --module backend.wsgi --buffer-size=100000 --chmod-socket=666 --master --processes 4 --threads 2