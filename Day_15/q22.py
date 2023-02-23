# 22 : Two numbers are entered through the keyboard. Write a program to find the value of one number raised to the power of another


def exponentation(num1, num2):
    return num1**num2


num1=int(input("Input num1 : "))
num2 = int (input("Input num2 : "))


print(exponentation(num1,num2))