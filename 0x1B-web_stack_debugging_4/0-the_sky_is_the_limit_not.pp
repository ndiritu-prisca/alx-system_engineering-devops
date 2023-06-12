#Fix stack to get 0 failed requests
exec { 'replace':
  path    => '/bin/',
  command => 'sed -i "s/15/4096" /etc/default/nginx',
}

exec { 'restart':
  path    => '/usr/bin/',
  command => 'service nginx restart',
}
