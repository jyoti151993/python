# 24 : Write a program with a function that accepts a string from keyboard and create a new string after converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses." the output should be "Stop And Smell The Roses"

def capitalize(str):
    return str.title()

str=input("Enter the string for eg stop and smell the roses")
print(capitalize(str))




        