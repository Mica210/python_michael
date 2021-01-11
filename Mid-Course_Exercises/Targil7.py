'''
 Write a Python program to convert height (in feet and inches) to
centimeters.
'''
from time import sleep

# print("\nConvert height imperial units to metric unit\n\nChoose your option\n---------")
# choise=input("1.Inches\n2.Feet\n")
# if(choise=="1"):
#     inch=float(input("Enter your height: "))
#     # sleep(1)
#     # print("\nYour height is: " + str("%.0f" % (inch*2.54)+ " cm."))
# elif(choise=="2"):
#     feet=float(input("Enter your height: "))
#     # sleep(1)
#     # print("\nYour height is: " + str("%.0f" % (feet*30.48) + " cm."))
# else:
#     print("\nChoose 1 or 2 only!!")

print("\nConvert height imperial units to metric unit\n\nChoose your option\n---------")
choise=input("1.Inches\n2.Feet\n")
imperial_h=float(input("Enter your height: "))
if(choise=="1"):
    print("\nYour height is: " + str("%.0f" % (imperial_h*2.54) + " cm."))
elif(choise=="2"):
    print("\nYour height is: " + str("%.0f" % (imperial_h*30.48) + " cm."))
else:
    print("Choose 1-2 only!!")