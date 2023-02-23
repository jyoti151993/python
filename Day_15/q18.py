# 18. Write a function in Python to count words in a text file "notes.txt" those are ending with alphabet "e"

def ends_with(s1):
   count = 0
   for i in s1:
       if str(i).endswith('e'):
           count +=1
   return count        

f=open("notes.txt", 'r')
s=f.read()
s1=s.split()
print("The count words in a text file those are ending with alphabet e : ",ends_with(s1))

