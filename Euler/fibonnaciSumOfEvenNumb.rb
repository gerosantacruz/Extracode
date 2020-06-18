#fibonnacu number
a =[1,2]
limit = 4000000

while a[-2] + a[-1] < limit
    a <<  a[-2] + a[-1] 
end

sum = 0

a.each { |x| sum += x if x.even? }
puts "The sum of the even fibonnaci number is #{sum}"
