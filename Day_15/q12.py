# Write a program to find the count of "triple" value in a string. 
# A "triple" in a string is a sequence of characters appearing thrice times in a row. 

# Return the count of triples in the given string. The triples may overlap

# Sample:

# triple_counter("defXXXdef") returns 1
# triple_counter("zzzabxxxxcd") returns 3 since xxx and xxx is present but in overlapping state 
# triple_counter("f") → 0



def triple_counter(string1):
    count=0
    for i in range(len(string1)-2):
        if string1[i]==string1[i+1]==string1[i+2]:
           count+=1
    return count      
      
words = "zzzabxxxxcd"  
print("No. of triplets in a given string ",triple_counter(words))
 
