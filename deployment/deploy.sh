#!/bin/bash
git clone https://github.com/we-race-here/flammerougeracing.git /home/jenkins/frr
cd /home/jenkins/frr
git checkout master
mkdir -p media

sudo cp -rf ../nginx.conf  /etc/nginx/nginx.conf
sudo cp -rf ../default.conf  /etc/nginx/sites-available/default
cp ../.env /home/jenkins/frr/
pip install uwsgi
#python manage.py collectstatic
python manage.py migrate

# Restart nginx
sudo /etc/init.d/nginx start || sudo /etc/init.d/nginx start

# Running Celery
#celery -A zp_result worker -l info &
#celery -A zp_result beat &
#nohup python manage.py zwift_bot &
#python manage.py whois_bot_start &
# Running Server
uwsgi --socket mysite.sock --module config.wsgi --buffer-size=100000 --chmod-socket=666 --master --processes 4 --threads 2