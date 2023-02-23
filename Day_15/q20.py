# 20. Create a text file named "matter.txt" contains some text, which needs to be displayed such that every next character is separated by a symbol "#".
# Write a function definition for hash_display() in Python that would display the entire content of the file matter.txt in the desired format.

# Example :
# If the file matter.txt has the following content stored in it :
# THE WORLD IS ROUND

# The function hash_display() should display the following content :
# T#H#E# #W#O#R#L#D# #I#S# #R#O#U#N#D#

def hash_display(words):
    new=""
    for word in words:
        new = new + word + "#"
    return new
f=open('matter.txt','r')
words=f.read()
print(words)
print(hash_display(words))
