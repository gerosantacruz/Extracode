

def palindrom():
    list_palindrom = []
    for i in range(0,1000):
        for x in range(0, 1000):
            num = i*x
            if str(num) == str(i*x)[::-1]:
                list_palindrom.append(num)
    return  max(list_palindrom)

        

#palindrom()


print(palindrom())