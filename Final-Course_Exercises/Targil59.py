'''
Write a Python program to convert height (in feet and inches) to
centimeters
'''

def convert():
    feet = float(input("Enter your height in feet: "))
    inch = float(input("Enter your height in inch: "))
    sum_f = feet * 30.48
    sum_i = inch * 2.54
    print(f'Converting feet to centimeters: {sum_f} .Cm \nConverting inch to centimeters: {sum_i} .Cm')

convert()