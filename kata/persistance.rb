def persistence(a)
  suma = 1
  step = 0   

  if a > 9
    a.to_s.each_char do |i| 
      suma *=i.to_i 
    end
    step += 1
    persistence(suma)
  else 
    return step 
  end
end

puts persistence(39)        
