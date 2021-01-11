'''
Write a Python program to print a specified list after removing the 0th,
4th and 5th elements
'''

list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(list)

list.pop(5)
list.pop(4)
list.pop(0)
print(list)