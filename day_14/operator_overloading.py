# ---------------------------------------
# Operator overloading Problems :
# ---------------------------------------
# Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno,Subject
# 	b) Instance Methods
# 	   get_subject
# 	   set_subject -- sets a subject for the particular instance
	 
# 	Main Method:
# 		Create two student objectsfor ex: Student1,Student2
# 		display subject names for each of the above created objects
# 		set a new subject name for each of the above created objects 	
# 		display subject names again after updating for each of the above created objects
		
# 		compare Student1,Student2 for >,<,>=,<=,== in some if else block [Should have 5 methods for each operator ]
# 			if the condition evaluate to true print "If clause successful"
# 			if the condition evaluate to false print "Else clause successful"
		
class Student:
     def __init__(self,name,roll_no,subject="Geography"):
        self.name=name
        self.roll_no=roll_no
        self.subject=subject
     def get_subject(self):
         print(self.subject)
     def set_subject(self,new_subject):
         self.subject=new_subject 
     def __gt__(self,other_student):
         return self.roll_no > other_student.roll_no
     def __lt_(self,other_student):
         return self.roll_no < other_student.roll_no
     def __le__(self,other_student):
         return self.roll_no <= other_student.roll_no
     def __ge__(self,other_student):
         return self.roll_no >= other_student.roll_no
     def __eq__(self, other_student) -> bool:
         print("Equals was invoked ..")
         return self.roll_no == other_student.roll_no   
    
        

student1 = Student("Raman",11,'English')
student2 = Student("Mohit",13,'Maths') 

print("Original subject of ",student1.name)
student1.get_subject()
student1.set_subject("Computer")
print("Updated subject of ",student1.name)
student1.get_subject()

print("Original subject of ",student2.name)
student2.get_subject()
student2.set_subject("Biology")
print("Updated subject of ", student2.name)
student2.get_subject()


# if student1 > student2:
#     print("if clause Successful")
# else:
#     print("else clause successful")    
    

# if student1 < student2:
#      print("if clause Successful")
# else:
#     print("else clause successful")  
       

# if student1 >= student2:
#     print("if clause Successful")
# else:
#    print("else clause successful")    
   

# if student1 <= student2:
#    print("if clause Successful")
# else:
#     print("else clause successful")      
     
if student1 == student2:
      print("if clause Successful")
else:
    print("else clause successful")
    
    
if student1 is student2 :
    print("Same student")
else:
    print("Different student")            