# Write a program to enter the numbers till the user wants and at the end the program should display the largest and smallest numbers entered


min=99999
max=0
choice = 'Y'
while choice=='Y' or choice =='y':
    num=int(input("Enter the number :  "))
    if num>max:
        max=num
    if num<min:
       min=num 
    choice=input("Do you wish to continue Y/N? ").upper()
print("Maximum number is ",max, "\n Minimum number is ",min)    
          
