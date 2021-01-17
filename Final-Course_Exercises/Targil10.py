'''
Write a Python program that accepts an integer (n) and computes the
value of n+nn+nnn
Sample value of n is 5
Expected Result : 615
'''



num=float(input("Enter a number: "))
sum=(num+(num*11)+(num*111))
print("The number is: " + str(sum))