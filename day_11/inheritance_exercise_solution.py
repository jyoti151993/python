"""
Exercise on Inheritance:
-------------------------
Create a base class named Employee as follows:
Employee (
-- class variables and methods
	organisation_name, 
	get_organisation_name(),
	set_organisation_name(org_name)

-- instance variables and methods()
emp_id,
name,
base_location,
deployed_location,
designation,
salary ,
get_employee_details() 	


Create a subclass of Employee named Manager as follows:
Manager(
	
	-- instance variables and methods()
	managed_employees[],
	perform_appraisal_for_an_employee(emp_id,percent_raise),
	get_manager_details(mgr_id)
)

Write a main method that does the following:
create 3 objects of Employee 
create an object of Manager_class and add the above 3 employee objects created as managed employees 
display get_manager_details()
for an employee do perform_appraisal_for_an_employee()
"""
class Employee:
    organisation_name= "Microsoft" 
    @classmethod
    def get_organisation_name(cls):
        return cls.organisation_name
    @classmethod
    def set_organisation_name(cls,rcv_organisation_name):
        cls.organisation_name =rcv_organisation_name
    def __init__(self,emp_id,name,base_location,deployed_location,designation,salary):
        self.emp_id =emp_id
        self.name=name
        self.base_location=base_location
        self.deployed_location=deployed_location
        self.designation=designation
        self.salary =salary
    def get_employee_details(self):
        print(self.emp_id,self.name,self.base_location,self.deployed_location,self.designation,self.salary,end="")

    def get_salary(self):
        return self.salary
    




class Manager(Employee):
    def __init__(self,name,base_location,deployed_location,designation,salary,rcvd_list,mgr_id):
        super().__init__(name,base_location,deployed_location,designation,salary)
        self.managed_employee = rcvd_list
        self.mgr_id=mgr_id
        
    def get_manager_details(self):
        super().get_employee_details()
        print(" ","Manager is managing employing :",self.managed_employee   , self.mgr_id )
    
    def perform_appraisal_for_an_employee(self,per_increment):
        self.salary = self.salary*(per_increment/100) +self.salary

emp1 = Employee(123,"Jyoti","pune","Mumbai","senior analyst",1000000)
emp2 = Employee(124,"Deepak","Bangalore","Mumbai","business development executive",100000)
emp3 = Employee(125,"Gaby","pune","Mumbai","system engineer",2000000)

emp1.get_employee_details()
emp2.get_employee_details()
emp3.get_employee_details()

lis =list(emp1,emp2,emp3)
manage_employee = Manager("Jay","pune","Mumbai","Department Manager",1000000000,lis, 101)
manage_employee.get_manager_details()
