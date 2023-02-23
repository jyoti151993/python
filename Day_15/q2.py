"""
2: Write a Python program that accepts number of subjects and then a list of subject names and a list marks.
Print subject name and marks in order of its first occurrence comma seperated.

Sample Input: 
Number of subjects: 3
Input Subject name : Bengali 
Input Subject name : English 
Input Subject name : Math 

Input Subject marks : 23
Input Subject name : 24
Input Subject name : 45


Sample output : 

Bengali--23 , English--24, Math--45

"""

no=int(input("Input no. of Subjects "))

sub_list=input("Input the comma separated Subject name : ").split(",")
print(sub_list)
marks_list=input("Input the comma separated marks ").split(",")
marks_list=[int(x) for x in marks_list]
print(marks_list)
sub_and_mrks={}
for i in range(no):
   sub_names=sub_list[i]
   sub_marks=marks_list[i]
   print(sub_names,"--",sub_marks)
#    if sub_names not in sub_and_mrks:
#        sub_and_mrks[sub_names]=sub_marks
#    else:
#        sub_and_mrks[sub_names]=sub_and_mrks[sub_names]+sub_marks
# disp_submrks=str(sub_and_mrks)
# print(disp_submrks.replace(":","-->"), end=" ")

#for i in range(no_of_sub):
    #sub_marks = int(input("Input the comma separated Subject marks : ")).split(",")
    #print(sub_name,"--",sub_marks)

        
    
    
     
     










  
    
    
    
    