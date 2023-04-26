#Install Nginx web server (w/ Puppet)

package {'nginx':
  ensure => 'present'
}

exec {'install':
  provider => shell,
  command  => 'sudo apt-get update; sudo apt-get -y install nginx,
}

exec {'run':
  provider => shell,
  command  => sudo service nginx start; sudo ufw allow 'Nginx HTTP',
}

exec {'Hello world!':
  provider => shell,
  command  => echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html,
}

exec {'redirect':
  provider => shell,
  command  => sed -i '/listen 80 default_server/a rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;' /etc/nginx/sites-available/default,
}

exec {'error':
  provider => shell,
  command  => sed -i "/redirect_me/ a\\\terror_page 404 /my_404.html;" /etc/nginx/sites-available/default; echo "Ceci n'est pas une page" | sudo tee /var/www/html/my_404.html,
}
