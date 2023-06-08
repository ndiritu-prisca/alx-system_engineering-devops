# Fix 500 error on Apache and automate using Puppet

exec { 'replace_php':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
