# 15. Write a function in Python to read lines from a text file "notes.txt". Your function should find and display the occurrence of the word "the".

# Note :
# Create a file "notes.txt" with the following content below:

# "India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most of the Indians can foresee the heights that India is capable of reaching."

# The output should be 5

def count_lines(s):
    count =0
    for i in s1:
        if str(i).upper() =='THE':
            count+=1
    return count      
    


f=open("notes.txt",'r')
s=f.read()
s1= s.split()
print("The count of the letter The is ", count_lines(s))
