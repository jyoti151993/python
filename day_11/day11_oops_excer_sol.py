"""
# **************** Refer introduction_to_oops.py for information 
---------------------------
Underscores usage in Python
---------------------------

Here is a quick summary of our 2 underscore patterns for naming conventions, which we have covered above.

Single Leading Underscore _var: Naming convention indicating name is meant for internal use. A hint for programmers and not enforced by programmers.
Double Leading Underscore __var: Triggers name mangling when used in class context. Enforced by the Python interpreter.

-------------------------------------------
Exercise 01 : Classes and objects -- try creating this in oops world
-------------------------------------------
Employee
  # instance variables 
   emp_id (Public)
   emp_salary (Private)
   mgr_id ( Public)
   
  # class variable 
  department_name
  
  # instance methods
  get_emp_salary()-> emp_salary
  set_emp_salary(rcv_salary)-> emp_salary

  # class method 
  get_department_name() --> department_name
  
  # static method
  field_expertice() --> just displays some expertise for all my employees
  
main

1) create an object employee(100,1000,1)  
2) do the following for the created object
// direct access using .notation
empid
emp_salary
mgr_id
3) print the department name 
4) display the expertise for the employees 
5) Deleting Attributes and Objects
 """
class Employee:
     department_name ='admin'
     
     def __init__(self, employee_id, emp_sal,mngr_id):
          self.emp_id= employee_id
          self.__emp_salary = emp_sal
          self.mgr_id = mngr_id
     def get_emp_salary(self):
          return self.__emp_salary
     def set_emp_Salary(self,rcvd_salary) :
            self.__emp_salary=rcvd_salary

     @classmethod
     def get_department_name(cls):
        return cls.department_name
     @classmethod
     def set_department_name(cls,rcvd_dept_name):
          cls.department_name = rcvd_dept_name


     @staticmethod
     def get_field_experience():
        print("Expertise in Data-Science,SME,sales ")


 #1) create an object employee(100,1000,1)
jayesh =Employee(100,500000,1)

print("The employee_id of my_new_employee", jayesh.emp_id)
print("The salary of my new employee", jayesh._Employee__emp_salary)
print("Manager id for my new employee", jayesh.mgr_id)
print("The department name is ", Employee.department_name)
 

Employee.get_field_experience()

print("Current Depart name",Employee.get_department_name())
Employee.set_department_name("Research & development")
print("Updated Jayesh's Salary is",Employee.get_department_name())

print("Current Salary of the Jayesh ", jayesh.get_emp_salary())
jayesh.set_emp_Salary(7000000)
print("Updated Salary ",jayesh.get_emp_salary())

print(jayesh.department_name)
print(dir(jayesh))
# Deleting Attributes and Objects
print("Before ", dir(Employee))
del (Employee.department_name)
print("After deleting --->", dir(Employee))

print("Before -->", dir(jayesh))
del(jayesh.emp_id)
print("After deleting -->", dir(jayesh))
