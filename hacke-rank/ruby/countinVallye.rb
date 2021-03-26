def countingValleys(steps, path)
    levelSea, valleys = 0, 0

    for item in 0..steps
        if path[item] == 'D'
            levelSea -= 1
        elsif path[item] == 'U'
            levelSea += 1
            if levelSea == 0
                valleys +=1
            end
        end

    end
    return valleys
end


puts countingValleys(8,'UDDDUDUU')


=begin
    
The challenge can be found in the next link:
https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
    
end