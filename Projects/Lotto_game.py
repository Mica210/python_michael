"""
Puts in a list of 6 numbers, between 1-37, as in a real lottery.
The numbers must not be repeated.
Each game (row) in Lotto costs 3 ILS, Insert how much money do you have?
Random 6 numbers – the winner's number.
Then play few rounds (rows) as your budget can handle.
On each round, random 6 numbers , between 1-37, and check if you won.
In the end sum the entire prize from all rounds.
If you guess:
6 numbers = won 1M ILS
5 numbers = won 5000 ILS
4 numbers = won 100 ILS
3 numbers = won 10 ILS
"""
from time import sleep
from random import randint


def lotto_game():
    global prize
    print("\nLets play the lottery.. \n")
    cash = int(input("\nEach game row costs 3 ILS \nPlease enter your amount: "))
    sleep(1)
    row = cash // 3
    print("\nYou have: " + str(row) + " rows\nYour change is: " + str(cash % 3) + " ILS\n")
    winning_num = []
    for i in range(0, 6):
        number = randint(1, 37)
        while number in winning_num:
            number = randint(1, 37)
        winning_num.append(number)
    sleep(1)
    print("=======================\nThe winning numbers are: \n" + str(winning_num) + "\n=======================\n")
    sleep(1)
    for i in range(row):
        print("\nRolling your numbers for row " + str(i + 1) + "\n---------------------")
        ran_num = []
        for x in range(0, 6):
            number = randint(1, 37)
            while number in ran_num:
                number = randint(1, 37)
            ran_num.append(number)
        print(ran_num)
        sleep(1)
        counter = 0
        for number in ran_num:
            if number in winning_num:
                counter += 1
        prize = 0
        print("\nyou guessed " + str(counter) + " number(s) correctly")
        if counter == 3:
            prize = prize + 10
            print("\ncongratulation !!! \nYou won 10 ILS")
        elif counter == 4:
            prize = prize + 100
            print("\ncongratulation !!! \nYou won 100 ILS")
        elif counter == 5:
            prize = prize + 5000
            print("\ncongratulation !!! \nYou won 5000 ILS")
        elif counter == 6:
            prize = prize + 1000000
            print("\ncongratulation !!! \nYou won 1M ILS")
        else:
            print("\nSorry try again!!")
    print("\n-----------------------------\nYou won total prizes of: " + str(prize) + " ILS.\nGoodbye")


lotto_game()
