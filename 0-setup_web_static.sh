#!/usr/bin/env bash
# preparing server for deployment

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install nginx
sudo service nginx start

# maybe don't want or need sudo
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo echo "Howdy" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data

# edit nginx cnfig file
find="^\tlocation / {"
replace="\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\n\tlocation / {"

sudo sed -i "s@${find}@${replace}@" /etc/nginx/sites-available/default

sudo service nginx restart
exit 0
