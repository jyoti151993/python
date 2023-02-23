# 16.Write a function display_words() in python to read lines from a text file "notes.txt", and display those words, which are less than 4 characters.

def display_words(Words):
    for word in Words:
        if len(str(word)) < 4:
         print(word) 
    
    

f=open("notes.txt",'r')
s=f.read()
Words=s.split()
display_words(Words)


    
