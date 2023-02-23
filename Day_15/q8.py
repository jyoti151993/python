# 8.Create a program that takes the user's current age as input and calculates how many days, weeks, and months they have left to live if they would get 99 years old.

# For this exercise, we assume that a year has 365 days, 52 weeks, and 12 months.We don't take leap years into account!

# Print the final result to the console using an f-String!

# Sample :
# Please enter your age today : 36
# Output :
# You have 22995 days, 3276 weeks, and 756 months left to live a joyful life !

from datetime import date

curr_age=int(input("Enter your age"))
res=99-curr_age
rem_days=365*res
rem_weeks=52*res
rem_months= 12*res
print(f"You have {rem_days} days, {rem_weeks} weeks, and {rem_months} months left to live a joyful life !")
