'''
Create a dictionary with 5 names & money
then sum the money of the first & last names and print it to the screen
after, add a new name with the sum of the money you calculated before
in the end, print the number of entries and check if "idan" is inside
'''


names_dict={"idan":55500,"yossi":25000,"moshe":33000,"dudu":11500,"kobi":5300}
print(names_dict)
sum=(names_dict["idan"])+(names_dict["kobi"])
print("\nThe summary of idan and kobi is: " + str(sum))
names_dict.update({"michael":sum})
print(names_dict)
print("\nThe number of entries: " + str(len(names_dict)))
print("Is the name idan is in the dict?: ")
print("idan" in names_dict)