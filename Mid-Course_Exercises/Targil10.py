'''
Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
'''

str1="Net4U"
my_dict = {}
for x in str1:
    my_dict[x] = my_dict.get(x, 0) + 1
print(my_dict)