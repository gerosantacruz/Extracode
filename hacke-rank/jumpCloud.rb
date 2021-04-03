
#!/usr/bin/ruby

def jumpingOnClouds(c)
    jump = 0
    index = 0
    while index <= (c.length()-1) do 
        
        if c[index] ==0 and c[index+1]== 1
            jump+=1
            index += 2
        elsif c[index] == 0 and c[index+1] == 0 and c[index+2]== 0
            jump+=1
            index+=2
        else
            index += 1
            jump+=1
        end
    end

    return jump-1
end
puts jumpingOnClouds([0,1,0,0,0,1,0])
puts jumpingOnClouds([0,0,0,1,0,0])
puts jumpingOnClouds([0,0,1,0,0,1,0])