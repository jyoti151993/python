"""Create a Student class with following 

a) instance variables 
   Name,Rollno,Subject
b) Instance Methods
   get_subject
   set_subject -- sets a subject for the particular instance
c) Class variables 
   school_name 
d) Class methods
	get_school_name
	set_school_name -- sets a school name for the class 
e) static methods
	display_prerequiste_skills --> displays some skills for all students in general good to have ones

Main Method:
	Create two student objects
	display subject names for each of the above created objects
	set a new subject name for each of the above created objects 	
	display subject names again after updating for each of the above created objects

	display the class variable 
	update the class variable using set_school_name method
	display the class variable 
	update the class variable using class_name. notation
	display the class variable 
	update the class variable using object_name. notation
	display the class variable 
	display the object variable with the same name as class variable for the object you selected on line27

	delete the school_name instance variable for the object you selected on line27
	display the object variable with the same name as class variable for the object you selected on line27

	delete the the object you selected on line27
	display the rollno for the object you selected on line27

	delete the school_name for the class
	display the class variable 


"""





class Student:

    school_name='ABPS'

    def __init__(self,rcv_name,rcv_roll_no,rcv_sub) :
        self.Name=rcv_name
        self.Roll_no=rcv_roll_no
        self.Subject=rcv_sub

    def get_subject(self):
        return  self.Subject

    def set_subject(self,rcvd_sub):
         self.Subject=rcvd_sub
             
    @classmethod
    def get_school_name(cls):
        return cls.school_name
    @classmethod
    def set_school_name(cls,rcvd_school_name):
        cls.school_name=rcvd_school_name
 

    @staticmethod
    def display_prerequisite_skills():
        print("The common pre-requsite for all the students are languages-(English,Hindi-->Grammar),class X std Maths, computer fundamentals & C-programming")


#Create two student objects
#display subject names for each of the above created objects
student1=Student('Gaby',221,"Economics")
student2=Student('Prabhat',222,"Accounts")

print(student1.get_subject())
print(student2.get_subject())


#set a new subject name for each of the above created objects 	
#display subject names again after updating for each of the above created objects

student1.set_subject("Statistics")
print(student1.get_subject())
student2.set_subject("Python")
print(student2.get_subject())



#display the class variable 

print(Student.get_school_name())
print(student1.get_school_name())
print(student2.get_school_name())

#update the class variable using set_school_name method

Student.set_school_name("Delhi Public School")


#display the class variable 
print(Student.get_school_name())

#update the class variable using class_name. notation
Student.school_name="St. Francis School"

#display the class variable 
print(Student.school_name)

#update the class variable using object_name. notation
student1.school_name="Chris Jyoti School"
student2.school_name="RYAN International School"


	#display the class variable
print("Updated school name using student1 reference ",student1.school_name)
print("Updated school name using student2 reference ",student2.school_name)

#display the object variable with the same name as class variable for the object you selected on line27
print(student1.school_name)
print(student2.school_name)

#delete the school_name instance variable for the object you selected on line27
print("Before deleting",dir(student1))
del(student1.school_name)
print("After deleting ", dir(student1))

#display the object variable with the same name as class variable for the object you selected on line27
student1.get_school_name()
print(student1.get_school_name())

#delete the the object you selected on line27
#del(student1)

#display the rollno for the object you selected on line27
print(student1.rollno)

#delete the school_name for the class
print("Before deleting ",dir(Student))
del(Student.school_name)
print("After deleting  ", dir(Student))

#display the class variable
print(Student.school_name) 


