# obejctive: create a piramid of one side using recursion

def pyramid(height):
    if height == 0:
        return

    pyramid(height-1)

    for i in range(height):
        print("#", end='')

    print('\n', end='')


pyramid(5)
