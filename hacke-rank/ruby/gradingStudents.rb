def grades(n)
    res = []

    n.each do |item|
        if item < 38
            res << item
        elsif ((item/5.0).ceil * 5 - item) >= 3
            res << item
        elsif ((item/5.0).ceil * 5 - item) < 3
            res << (item/5.0).ceil * 5
        end
    end

    return res
end

puts grades([75,67,38,33])