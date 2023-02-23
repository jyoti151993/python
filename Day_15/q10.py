# 10.
# create a class named "CDAC_course"   
# class variable 
# 	instructors_so_far_for_the_course[] // list 
# instance variables 
# 	subject_name (public)
# 	subject_instructor_name (public)
# 	subject_instructor_designation ( protected)
# 	subject_instructor_company ( protected)
# 	subject_instructor_feedback ( private)

# instance methods
#    get_subject_instructor_feedback()

# classmethod   
#    get_instructors_so_far_for_the_course()
#    // append to the existing list in this func
#    set_instructors_so_far_for_the_course(instructor_name) 

# create a function main that 
# a) creates an obj of course class with values
#    DIOT-Python,Elon Musk,CEO at Tesla ,Cdac,"Sample Feedback"
# b) Add Elon musk to the class list variable instructors_so_far_for_the_course
# c) print Elon Musk feedback
# d) Print all the  instructors_so_far_for_the_course  


class CDAC_course:
    instructors_so_far_for_the_course=[] 
    
    def __init__(self, sub_name,sub_inst_name,sub_inst_design,	sub_inst_comp,sub_inst_feedback):
        self.subject_name = sub_name
        self.subject_instructor_name = sub_inst_name
        self._subject_instructor_designation = sub_inst_design
        self._subject_instructor_company = 	sub_inst_comp
        self.__subject_instructor_feedback = sub_inst_feedback
        
    def get_subject_instructor_feedback(self):
         return self.__subject_instructor_feedback
     
      #classmethod   
#    get_instructors_so_far_for_the_course()
#    // append to the existing list in this func
#    set_instructors_so_far_for_the_course(instructor_name)

    @classmethod
    def get_instructors_so_far_for_the_course(cls):
        return cls.instructors_so_far_for_the_course
    @classmethod 
    def set_instructors_so_far_for_the_course(cls,rcvd_inst):
       cls.instructors_so_far_for_the_course.append(rcvd_inst)
       
pg_diot = CDAC_course('DIOT-Python','Elon Musk','CEO at Tesla' ,'Cdac','Sample Feedback')
CDAC_course.set_instructors_so_far_for_the_course("Elon Musk")
print(CDAC_course.get_instructors_so_far_for_the_course())
res=pg_diot._CDAC_course__subject_instructor_feedback
print(res)
print(CDAC_course.instructors_so_far_for_the_course)

       
     