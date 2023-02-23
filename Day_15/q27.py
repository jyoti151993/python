    # """"" 27: Write a program that keeps student's name 
    # and his marks in a dictionary as key-value pairs.
    # The program should store records of 10 students and 
    # display students name and marks of five students in 
    # decreasing order of marks obtained. """""
    
    
dict={}
list=[]
    
for i in range(10):
 name, marks=input("Enter the student name and marks: ").split()
 list.append((marks,name))
 
list=sorted(list, reverse=True)

print("Sorted list of students according to their marks in descending order")
for i in list:
 print(i[1][0])    


     
      

