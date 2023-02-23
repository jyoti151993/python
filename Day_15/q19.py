#  Write a function in Python to count uppercase character in a text file "notes.txt"
def count_uppercase(s1):
    count = 0;
    for i in s1:
       if str(i).isupper():
           count+=1
    return count


f=open("notes.txt", 'r')
s=f.read()
s1=s.split()
print("The count of upper case charcter in notes.txt is : ", count_uppercase(s1))