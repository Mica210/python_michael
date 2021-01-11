'''
Write a Python program to sum all the items in a list.
'''

list=[1,2,3,4,5,6,7]
sum=0
for x in range(len(list)):
    sum=sum+list[x]

print(sum)