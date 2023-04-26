#Install Nginx web server (w/ Puppet)

exec {'install':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx; sudo service nginx start; sudo ufw allow 'Nginx HTTP'; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html; sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default; sed -i "/redirect_me/ a\\\terror_page 404 /my_404.html;" /etc/nginx/sites-available/default; echo "Ceci n'est pas une page" | sudo tee /var/www/html/my_404.html'
}
