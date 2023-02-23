# 6. Write a Python program to count the occurrence of each element of a given list. 

# Sample :
# Original List:
# ['Green', 'Red', 'Blue', 'Red', 'Orange', 'Black', 'Black', 'White', 'Orange']

# Count the occurrence of each element of the said list:
# Counter({'Red': 2, 'Orange': 2, 'Black': 2, 'Green': 1, 'Blue': 1, 'White': 1})

# Original List:
# [3, 5, 0, 3, 9, 5, 8, 0, 3, 8, 5, 8, 3, 5, 8, 1, 0, 2]

# Count the occurrence of each element of the said list:
# Counter({3: 4, 5: 4, 8: 4, 0: 3, 9: 1, 1: 1, 2: 1})


# def countx(lst,x):
#      count=0
#      for elem in lst:
#          if (elem==x):
#              count=count+1
#              return count
    
    
    
# lst= input("Enter the comma separated values such Red, Blue, Orange: ").split(",")
# print(lst)
# x=input("Please input value(color), for which you want to make a count ")
# print(f"{x} has occured {countx(lst,x)} times")
    
    
    
    
    
ls = input("Please input the comma separarted values ").split(",")
occurence={ item:ls.count(item) for item in ls}
print(occurence.get(input("Enter the value to be  counted from list ")))    