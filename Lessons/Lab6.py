'''
Write a code that will show a menu:
1.Insert Number and ** it by 3.
2.insert 4 IPs to a list and print it.
3.Insert 4 Entries to dns_Dictionary and print it.
4.check if a string is polindrom

if the user wont choose 1-4, you will tell him to insert ony 1-4.
'''
from time import sleep
print("Starting the menu... \n")
sleep(1)
choise=input("Menu\n______\n" + "1.Enter a number to ** it by 3: \n" + "2.Enter 4 IP Addresses and print them: \n" + "3.Enter 4 Entries to dns_Dictionary and print them: \n" + "4.check if a string is polindrom \n")
if(choise=="1"):
    print("Your new number is: " + str((int(input("Enter a number: ")))**3))
elif(choise=="2"):
    IP_lists=[]
    IP_lists.append(input("Enter your IP:"))
    IP_lists.append(input("Enter your IP:"))
    IP_lists.append(input("Enter your IP:"))
    IP_lists.append(input("Enter your IP:"))
    sleep(1)
    print("\nYour IP lists is: " + str(IP_lists))
elif (choise=="3"):
    DNS_dict={}
    DNS_dict.update({input("Enter your URL:"): input("Enter IP: ")})
    DNS_dict.update({input("Enter your URL:"): input("Enter IP: ")})
    DNS_dict.update({input("Enter your URL:"): input("Enter IP: ")})
    DNS_dict.update({input("Enter your URL:"): input("Enter IP: ")})
    sleep(1)
    print("\nYour DNS_Dictionary is:\n" + str(DNS_dict))
elif(choise=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("This is polindrom!!")
    else:
        print("This isn't polindrom!!")
else:
    print("Enter 1-4 only!!!")