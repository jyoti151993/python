# 14. Below we've provided a list of tuples, where each tuple contains details about an employee of a shop. 
# Print how much each employee is due to be paid at the end of the week in a nice, readable format.
"""
Below we've provided a list of tuples, where each tuple contains details about an employee of a 
shop(their name, the number of hours worked last week, and their hourly rate). Print how much each employee is
 due to be paid at the end of the week in a nice, readable format.
employees = [ ("Rolf Smith", 35, 8.75), ("Anne Pun", 30, 12.50), ("Charlie Lee", 50, 15.50), ("Bob Smith", 20, 7.00) ]
"""
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
print("The weekly wages of the employees are as follows : ")
for emp in employees:
    print("Employee name : ", emp[0])
    print("Weekly wages: Rs", emp[1]*emp[2])
    