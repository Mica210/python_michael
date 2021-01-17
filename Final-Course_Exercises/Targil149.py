'''
Write a Python function that takes a positive integer and returns the sum
of the cube of all the positive integers smaller than the specified number.
'''


def positive(num):
    sum = 0
    for i in range(1,num):
        sum = sum + (i**3)
    print("The summery is: " + str(sum))
    return sum

new_num = positive(int(input("Enter a positive number: ")))