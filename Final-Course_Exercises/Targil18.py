'''
Write a Python program to calculate the sum of three given numbers, if
the values are equal then return three times of their sum.
'''


def sum_trios(x , y , z):
    sum = x + y +z
    if(x == y == z):
        sum = sum * 3
    return sum


print(sum_trios(1 , 1 , 1))


