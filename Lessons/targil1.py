print("Now we will calculte your marking:\nPrices:\n------\nTomato=3 NIS\ncucumber=2 NIS\nCola=5 NIS\nChicken=20 NIS\n")
tomatos=int(input("Enter how many tomatos?"))
cucumbers=int(input("Enter how many cucumbers?"))
colas=int(input("Enter how many colas?"))
chickens=int(input("Enter how many chickens?"))

print("\nSummary of your order:\n---------\ntomatos: " + str(tomatos) + "\ncucumbers: " + str(cucumbers) + "\ncolas: " + str(colas) + "\nchickens: " + str(chickens))

summary=(tomatos*3)+(cucumbers*2)+(colas*5)+(chickens*20)
print("\nYour total price is: " + str(summary) + " Nis without tax")
print("\nYour total price is: " + str("%.1f" % (summary*1.17)) + " Nis with tax")
