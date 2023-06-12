#Change the OS configuration so that it is possible to login with the holberton
#user and open a file without any error message.
$hard_limit = 50000
$soft_limit = 50000

exec { 'increase_hard_limit':
  path    => '/usr/local/bin/:/bin/',
  command => "sed -i \"/holberton hard/s/5/${hard_limit}/\" /etc/security/limits.conf",
}

exec { 'increase_soft_limit':
  path    => '/usr/local/bin/:/bin/',
  command => "sed -i \"/holberton soft/s/4/${soft_limit}/\" /etc/security/limits.conf",
}
