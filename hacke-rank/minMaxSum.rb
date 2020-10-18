arr = [1,3,5,7,9]

te = arr.clone

res = []

for i in 0..4 
    te.delete_at(i)

    res.push(te.sum)

    te = arr.clone
end
resu = res.minmax
puts resu.join(" ")

