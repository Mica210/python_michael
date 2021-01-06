
'''
Create a list with 4 details about you: name, age, mail, phone and print it to the screen
then create another list with 2 IPs , then add 3 more IPs , pop the 3rd IP and print how many
IPs do we have and print them.
'''


list=["Michael" , 34 , "mica@walla.com" , "0545454545"]
print("My name is: " + list[0] + "\nMy Age is: " + str(list[1]) + "\nMy Email is: "+ list[2] + "\nMy Phone is: " + list[3])

ip_list=["192.168.1.0","192.168.1.1"]
print(ip_list)

ip_list.append("192.168.1.2")
ip_list.append("192.168.1.3")
ip_list.append("192.168.1.4")
print(ip_list)

ip_list.pop(2)
print(ip_list)

print("IP list length is: " + str(len(ip_list)) + "\nAnd the IP address are: " + str(ip_list))