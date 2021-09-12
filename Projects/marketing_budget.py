"""Create a code that will ask for your marketing budget.
 Facebook campaign = 100ILS per day.
 Instagram campaign = 50ILS per day.
Ask him:
How long he wants the Facebook campaign will run.
How long he wants the Instagram campaign will run.
Then print to the screen the summary of the cost in ILS with tax (17%)
If it is more than his marketing budget, tell him how much to add, if not tell him "successful"."""
from time import sleep


def marketing():
    print("\nWelcome to marketing campaign\n---------------\nFacebook campaign = 100 ILS per day\nInstagram campaign "
          "= 50 ILS per day\n")
    budget = int(input("\nEnter your marketing budget: "))
    campaign = int(input("\nEnter number of facebook campaign days: ")) * 100 + (int(input("Enter number of instagram "
                                                                                           "campaign days: ")) * 50)
    summary = (round(campaign * 1.17))
    sleep(1)
    print("\nYour summary for the campaigns include tax: " + str(summary) + " ILS")
    sleep(1)
    if summary > budget:
        print("\nYour budget is to low please add : " + str(summary - budget) + " ILS")
    else:
        print("\nYour change is: " + str(budget - summary) + " ILS\n\nsuccessful")


marketing()

