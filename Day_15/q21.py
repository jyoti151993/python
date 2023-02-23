# 21. Write a function character_A_M_Count() in Python, which should read each character of a text file STORY.TXT.
# It should count and display the occurance of alphabets A and M (including small cases a and m too).

# Create a text file STORY.TXT with the below contents:

# Updated information
# As simplified by official websites.


# The character_A_M_Count() function should display the output as:

# A or a:4
# M or m :2

def  character_A_M_Count(s):
        
     count_A=s.count('A')
     count_a=s.count('a')
     count_M=s.count('M') 
     count_m=s.count('m') 
     print(f"count of A or a : {count_A+count_a}, count of M or m: {count_M+count_m}")


f=open("STORY.TXT",'r')
s=f.read()

character_A_M_Count(s)

