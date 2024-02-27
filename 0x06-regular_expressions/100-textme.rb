#!/usr/bin/env ruby
puts ARGV[0].scan(/([A-Za-z]*(^\d10,10)?),[([A-Za-z]*(^\d10,10)?)],[([A-Za-z]*(^\d10,10)?)]/).join
