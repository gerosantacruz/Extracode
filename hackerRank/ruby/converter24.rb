require 'date' 

time = "12:00:00AM"

t = DateTime.parse(time)

puts DateTime.parse(time).strftime('%H:%M:%S').to_s



