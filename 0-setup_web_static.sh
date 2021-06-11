#!/usr/bin/env bash
# setup server for web static

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
htmlvar="<html>\n <head>\n </head>\n <body>\n\tHolberton School\n </body>\n</html>"
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo echo -e "$htmlvar" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i "s@^\tlocation / {@\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n\n\tlocation / {@" /etc/nginx/sites-available/default
sudo service nginx restart
exit 0
