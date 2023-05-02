# automate the task of creating a custom HTTP header response, but with Puppet.
class webserver {
  # Updating package repository
  exec { 'apt-get update':
    path   => '/usr/bin',
    onlyif => 'test -e /usr/bin/apt-get',
  }

  # Installing nginx
  package { 'nginx':
    ensure  => installed,
  }

  # Starting nginx
  service { 'nginx':
    ensure => running,
    enable => true,
  }

  # Allow HTTP traffic
  exec { 'allow-http':
    command => 'ufw allow \'Nginx HTTP\'',
    path    => '/usr/bin',
    require => Package['ufw'],
  }

  # Creating index file
  file { '/var/www/html/index.nginx-debian.html':
    content => 'Hello World!',
    require => Service['nginx'],
  }

  # Configuring nginx server
  file { '/etc/nginx/sites-available/default':
    ensure => present,
    content => template('webserver/nginx.conf.erb'),
    notify => Service['nginx'],
  }

  # Creating a 404 page
  file { '/var/www/html/my_404.html':
    content => "Ceci n'est pas une page",
    require => Service['nginx'],
  }
}
