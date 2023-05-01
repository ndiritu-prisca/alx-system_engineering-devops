#Install Nginx web server (w/ Puppet)

exec { 'apt-update':
  command => 'apt-get update',
}

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure => running,
  enable => true,
}

exec { 'nginx-ufw':
  command => 'ufw allow \'Nginx HTTP\'',
}

file { '/var/www/html/index.nginx-debian.html':
  content => 'Hello World!',
}

file_line { 'nginx-redirect':
  path  => '/etc/nginx/sites-available/default',
  line  => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
  match => '^listen 80 default_server',
}

file_line { 'nginx-error-page':
  path  => '/etc/nginx/sites-available/default',
  line  => 'error_page 404 /my_404.html;',
  match => 'redirect_me',
}

file { '/var/www/html/my_404.html':
  content => 'Ceci n\'est pas une page',
}

