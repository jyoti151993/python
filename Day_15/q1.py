# Write a Python program that accept a number of words and then those number of words and Print the number of distinct words and number of occurrences for each distinct word according to their appeara
  
word_list=[]
limit=int(input("Enter the number of words  "))
print("Enter the words ")
for i in range(limit):
  str=input().lower()
  word_list.append(str)

my_dict={}
for w in word_list:
     if w not in my_dict:
         my_dict[w]=1
     else:
         my_dict[w]+=1


print("Number of distinct words = ",len(my_dict))
for i in my_dict:
    print(i,my_dict[i]) 
    
