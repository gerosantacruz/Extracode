def plusMinus(arr)
    result = [0,0,0]
    arr.each do |item|
        if item < 0
            result[1] += 1
            
        elsif item > 0
            result[0] += 1
        else
            result[2] += 1
        end
    end

    result = ['%1.6f'% ( result[0].to_f / arr.length ),
    '%1.6f'% (result[1].to_f / arr.length),
    '%1.6f'% (result[2].to_f / arr.length)]

    return result

end


puts plusMinus([-4, 3, -9, 0, 4,1])

