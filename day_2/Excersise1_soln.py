#1) Accept two numbers from the user and print 

#a) addition
num1=int(input("Enter the first number ::: "))
num2=int(input("Enter the second number ::: "))
my_addition=num1+num2
print("The sum of num1 and num2 is ",num1,num2,my_addition)

 
#b) first number squared 2
num1=int(input("Enter the first number ::: "))
my_square=num1**2
print("The square of the num1 is ",my_square)

#c) first number raised to number second number
num1=int(input("Enter the first number ::: "))
num2=int(input("Enter the second number ::: "))
raised_num=num2**num1
print("num2 raised to num1 is :",raised_num)


#2) Accept String from user and output upper case of the input string 

my_str=input("Enter your string :::: ")
print("The upper case of the entered string :: ",my_str.upper())

#3) Define a variable named "raise_salary_percentage" and get the salary raise 
#percentage from the user, Now apply the raise to an employee
#with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
#print the incremented salary to the console

Name='Gaurav'
existing_salary=900
percentage=int(input("Enter your hike percentage"))
raised_salary_percentage =existing_salary+(existing_salary*percentage/100)
print("The name of employee,his/her existing salary and inc salary are ",Name,existing_salary,raised_salary_percentage)


#4) Get the height from the user in cms and display the user height back to consolein foot/feet and inches