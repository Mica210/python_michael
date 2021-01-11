'''
Lab7- Cube project
נקבל כקלט כמה כסף יש לנו לשחק
עלות משחק 3 ש"ח
אם יש עודף נחזיר אותו ללקוח
בכל תור נגריל 2 קוביות , אם הן זהות זכינו ב- 100 ש"ח, אם הן זהות אבל שוות גם ל-6, זכינו ב- 1000 ש"ח
אם הן לא זהות, אבל קוביה 2 שווה ל-2 זכינו ב- 40 ש"ח
אם הן לא זהות אבל קוביה 1 שווה ל-1 זכינו ב- 20 ש"ח
לבסוף נדפיס למסך בכמה כסף זכינו
'''
from random import randint
from time import sleep

print("Lets play a dice game.. \nEach game cost 3 NIS\n")
cash=int(input("Please enter your amount: "))
sleep(1)
game=cash//3
print("You have: " + str(game) + " games\nyour change is: " + str(cash%3) + " NIS\n")
prize=0
for x in range(game):
    print("Rolling Dice for Round .. " + str(x+1) + "\n------------\n")
    sleep(1)
    die1=randint(1,6)
    die2=randint(1,6)
    print("Die1: " + str(die1) + "\nDie2: " + str(die2) + "\n")
    if(die1==die2):
        if(die1==6):
            prize=prize+1000
        else:
            prize=prize+100
    elif(die1==1):
        prize=prize+20
    elif(die2==2):
        prize=prize+40
sleep(1)
print("You won: " + str(prize))