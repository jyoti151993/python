# 3.Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda function. I

# Input number of students, names and grades of each student. 

# Sample Input:
# Input number of students: 3
# Name: Avik Das
# Total marks: 89
# Name: ayan Roy
# Total marks: 75
# Name: Sayan Dutta
# Total marks: 93

# Sample Output:
# Names and Marks of all students:
# [['Avik Das ', 89.0], ['ayan Roy', 75.0], ['Sayan Dutta', 93.0]]

# Second lowest Marks: 89.0
# Names: Avik Das

student_list=[]
total_marks_list=[]
second_lowest=0
n=int(input("Input the number of students:  "))

new_list=[]
for i in range(n):
    s_name = input("Name: ")
    t_marks = int(input("Total Marks: "))
    student_list.append([s_name,t_marks])
print("Names and Marks of all students : ")
print(student_list)
ordered_l =sorted(student_list,key = lambda x: int(x[1]))
print(ordered_l)
for j in range(n):
    if ordered_l[j][1] != ordered_l[0][1]:
        second_lowest=ordered_l[j][1]
        break
print("Second lowest marks ", second_lowest)  
sec_student_name=[x[0] for x in ordered_l if x[1]==second_lowest]
sec_student_name.sort()
print("\n Names :")
for s_names in sec_student_name:
    print(s_name)  




