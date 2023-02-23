# ---------------------------------------
# Inheritance Problems :
# ---------------------------------------
# 1) Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno(private),Subject (Protected)
# 	b) Instance Methods
# 	   get_subject 
# 	   set_subject -- sets a subject for the particular instance
	   
# 	   get_rollno
# 	   set_rollno -- sets a rollno for the particular instance

# 	   display_student_details -- > prints the name,rollno,subject 
# 	   get_primary_skill --> prints the primary skill
# 	   set_primary_skill --> sets the primary skill
	   
# 	Create a subclass named DBDA_student with following 
# 	a) instance variables 
# 	   Name,Rollno(private),Subject(protected), primary_skill,secondary_Skills(an array of other skills other than primary skill)
# 	b) Instance Methods
# 	   get_subject
# 	   set_subject -- sets a subject for the particular instance

# 	   get_rollno
# 	   set_rollno -- sets a rollno for the particular instance

# 	   display_student_details -- > prints the name,rollno,subject,primary_skill,secondary_skills
	   
# 	   Override the set_primary_skill method to always have SQL as primary skill
	   

# 	Main Method:
# 		Create two DBDA student objects for ex: Student1,Student2
# 		display subject names for each of the above created objects
		
# 		display rollno for each of the above created objects
# 		set a new subject name for each of the above created objects 	
# 		display subject names again after updating for each of the above created objects
		
# 		compare Student1,Student2 for > in some if else block
# 			if the condition evaluate to true print "If clause successful"
# 			if the condition evaluate to false print "Else clause successful"

# 		set the primary skill for Student1	
# 		print the primary skill for Student1
# 		print the primary skill for Student2


# 1) Create a Student class with following 

# 	a) instance variables 
# 	   Name,Rollno(private),Subject (Protected)
# 	b) Instance Methods
# 	   get_subject 
# 	   set_subject -- sets a subject for the particular instance

Student1 =