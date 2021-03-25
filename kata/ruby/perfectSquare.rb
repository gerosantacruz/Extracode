def is_square(x)

    root = Math.sqrt(x).to_int()
    if x == root * root
        return true
    else
        return false
    end
    
end


puts is_square(25)