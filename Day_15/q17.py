
# 17. Write a function in Python to count the words "this" and "these" present in a text file "notes.txt". 
# [Note that the words "this" and "these" are complete words]

def count_words(s1):
    count =0
    for i in s1:
        if str(i).lower() =='this' and str(i).lower() == 'these':
           count +=1 
    return count



f=open("notes.txt",'r')
s=f.read()
s1=s.split()
print("The count of 'this & 'these' ", count_words(s1))
