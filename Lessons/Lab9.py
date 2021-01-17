'''
Menu:
1.Dogs Details
2.Friends list
3.N Azzeret
'''

def menu():
    while(True):
        choice=(input("Menu\n-------\n1.Dogs Details\n2.Friends list\n3.N Azzeret\n"))
        if(choice=="1"):
            Dogs()
        elif(choice=="2"):
            Friends()
        elif(choice=="3"):
            Azzeret()
        else:
            print("Enter 1-3 only!!")
            continue
        Exit=input("\nDo you want to exit? yes/no: ")
        if(Exit=="yes"):
            break
        else:
            print("Welcome back\n ")
    print("\nBye Bye\n")

def Dogs():
    name=input("Enter a dog name: ")
    age=int(input("Enter a dog age: "))
    print("Your dog name is: " + name + "\nYour dog age is: " + str(age*7))

def Friends():
    friends_list=[]
    for i in range(5):
        friends_list.append(input("Enter a friend name: "))
    print(friends_list)
    name=input("Enter a new name: ")
    if(name in friends_list):
        print("The name exist!!")
    else:
        print("The name isn't exist")
def Azzeret():
    num=int(input("Enter a number: "))
    sum=1
    for i in range(1,num+1):
        sum *= i
    print(str(num) + " Azzeret is " + str(sum))


menu()

