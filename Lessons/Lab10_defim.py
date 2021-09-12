from time import sleep


def menu():
    while True:
        choice1 = input("Menu\n-------\na.IP System\nb.DNS System\n")
        if choice1 == "a":
            choice2 = input("\nIP_Menu\n-------\n1.Search for IP address from a list\n2.Add IP address to a "
                            "list\n3.Delete IP address from a list\n4.Print all the IP list\n")
            if choice2 == "1":
                search_ip()
            elif choice2 == "2":
                add_ip()
            elif choice2 == "3":
                delete_ip()
            elif choice2 == "4":
                print_list()
        elif choice1 == "b":
            choice3 = input("\nDNS_Menu\n-------\n1.Search for URL from a dictionary\n2.Add URL + IP address to a "
                            "dictionary\n3.Delete URL from a dictionary\n4.Update the IP address of specific "
                            "URL\n5.Print all URL:IP dictionary\n")
            if choice3 == "1":
                search_url()
            elif choice3 == "2":
                add_url_ip()
            elif choice3 == "3":
                delete_url()
            elif choice3 == "4":
                update_url()
            elif choice3 == "5":
                print_dict()
        else:
            print("\nEnter A-B only!")
            continue
        exit = input("\nDo you want to exit? yes/no: ")
        if exit == "yes":
            break
        else:
            print("\nWelcome back\n ")
    print("\nBye,Bye")


def search_ip():
    filename = "C:/Users/מיכה/Documents/IP_addresses.txt"
    file = open(filename, "r")
    ip_list = file.read()
    ip_s = input("Enter ip to search: ")
    sleep(1)
    if ip_s in ip_list:
        print("The IP exist!!")
    else:
        print("The IP isn't exist")
    file.close()


def add_ip():
    filename = "C:/Users/מיכה/Documents/IP_addresses.txt"
    file = open(filename, "a")
    file.write(input("\nEnter a new ip: " + "\n"))
    sleep(1)
    print("\nDone\n")
    file.close()


def delete_ip():
    filename = "C:/Users/מיכה/Documents/IP_addresses.txt"
    file = open(filename, "r")


def print_list():
    filename = "C:/Users/מיכה/Documents/IP_addresses.txt"
    file = open(filename, "r")
    print(file.read())
    file.close()


DNS_dict = {"www.google.com": "8.8.8.8", "www.youtube.com": "7.7.7.7", "www.twitter.com": "6.6.6.6",
            "www.facebook.com": "5.5.5.5"}


def search_url():
    url_name = input("Enter URL: ")
    sleep(1)
    if url_name in DNS_dict:
        print("The URL exist !!")
    else:
        print("The URL isn't exist")


def add_url_ip():
    DNS_dict.update = ({input("Enter your new URL:"): input("Enter IP: ")})
    sleep(1)
    print("\nDone\n")


def delete_url():
    del DNS_dict[input("Enter URL: ")]
    sleep(1)
    print("\nDone\n")


def update_url():
    DNS_dict[input("Enter exist URL:")] = input("Enter new IP: ")
    sleep(1)
    print("\nDone\n")


def print_dict():
    print(DNS_dict)


menu()
