
'''
Create 2 variables : string of your full name, another string of your mail.
Create variable of your age (integer)
print all of them to the screen
then Print your name from the end to the beginning and print it only with your age*3
then check if your name is stored inside this full string:
"idan ben dudu yuval shimon yael gal adam shahar yana"
'''

name="Michael"
age=34
mail="mica@walla.com"

print("My name is: " + name + "\nMy age is: " + str(age) + "\nMy mail is: " + mail)
print("\nMy reverse name is: " + name[::-1] + "\nMy multiple age is: " + str(age*3))
print("Michael" in "idan ben dudu yuval kobi shimon gal yael")

