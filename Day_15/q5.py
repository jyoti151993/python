# Write a Python program to count most and least common characters in a given string.

# Sample :
# Original string:
# hello world
# Most common character of the said string: l
# Least common character of the said string: h

from collections import Counter
def max_least_char(str1):
    temp=Counter(str1)
    max_char=max(temp,key=temp.get)
    min_char=min(temp,key=temp.get)
    return(max_char,min_char)

str1="hello world"
print("Original String")
print(str1)
result=max_least_char(str1)
print("\nMost common character of the said string: ",result[0])
print("least common character of the said string: ", result[1])