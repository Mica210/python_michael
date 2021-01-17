'''
Write a Python program to calculate number of days between two dates.
'''

from datetime import date

first_date = date(2014, 7, 2)
second_date = date(2014, 7, 11)

sum_days = second_date - first_date
print("\nTotal days: " + str(sum_days))
