'''
Write a Python script to add a key to a dictionary.
'''

my_dict={"a":10,"b":20,"c":30,"d":40}
print("Your current dictionary is: " + str(my_dict))
my_dict.update({input("Enter a new letter:"): input("Enter a new number: ")})
print("Your new dictionary is: " + str(my_dict))