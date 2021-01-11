'''
Write a Python program which accepts the user's first and last name
and print them in reverse order with a space between them.
'''

name=(input("Enter your full name: "))
print(name)
print(' '.join(name[::-1]))