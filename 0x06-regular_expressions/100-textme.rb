#!/usr/bin/env ruby
#puts ARGV[0].scan(/.*from:([^\]]+).*to:([\+\d]+).*flags:([-\d:]+).*/).join
match = ARGV[0].match(/.*from:([^\]]+).*to:([\+\d]+).*flags:([-\d:]+).*/)
#match = ARGV[0].match(/.*from:(\D?[\w]*).*to:(\D\d*).*flags:([\D+\d]{12}).*/)
output = "#{match[1]},#{match[2]},#{match[3]}"
puts output
