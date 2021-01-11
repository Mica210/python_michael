'''
Write a Python program to accept a filename from the user and print
the extension of that
'''


filename = input("Enter the Filename: ")
a = filename.split(".")
print ("The extension of the file is : " + str(a[-1]))

