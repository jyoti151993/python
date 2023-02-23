# regular function
def my_addition(first_num, second_num):
    """receives two numbers from the invoking application and returns addition """
    return first_num + second_num


# invoking regular function
print(my_addition(1, 2))

# lambda function
# lambda inputparam : return_expression
my_lamdba_add_func = lambda first_num, second_num: first_num + second_num

# invoking lambda function
print(my_lamdba_add_func(1, 2))


# definitions
def my_square(first_num):
    """receives two numbers from the invoking application and returns first number squared 2 """
    return str(first_num ** 2)


my_lambda_square_func = lambda first_num: str(first_num ** 2)


# invocation
print(my_square(5))
print(my_lambda_square_func(5))

# Higher order function
def my_higher_order_func(l_func, *args):
    print(f"I am higher order function with arguments {l_func, *args}")
    print(l_func(*args))


# invocation of HOF
my_higher_order_func(my_lambda_square_func, 5)
my_higher_order_func(my_lamdba_add_func, 1, 2)

"""
# -----------------------------------------------------------------------
# EXERCISE on lambda and Higher Order Functions
# -----------------------------------------------------------------------
# 1) ******** Convert following functions from function_definitions.py into lambda *****    
# 2) ******** Create HOF so that each of the above created lambda functions can be invoked 
#             using a single HOF *****                
# """

# 1) Accept two numbers from the user and print
# a) addition
add_two_num = lambda first_num, second_num : first_num+second_num
print(add_two_num(5,2))


# b) first number squared 2
square_num = lambda first_num: str(first_num**2)
print(square_num(5))
# c) first number raised to number second number
raised_num = lambda first_num, second_num : first_num**second_num
print(raised_num(5,2))
#
# 2) Accept String from user and output upper case of the input string
upper_case = lambda a=input("Enter a string  ") : a.upper()
print(upper_case())

#
# 3) Define a variable named "raise_salary_percentage" and get the salary raise
# percentage from the user, Now apply the raise to an employee
# with harcoded data Name= 'gaurav' existing_salary = 900 INR and
# print the incremented salary to the console




#
# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches
h=166
get_height_ft= lambda ht: ht//30.48
get_height_inches= lambda ht: round((ht/2.54)%12,1)
print(f"{get_height_ft(h)} feet {get_height_inches(h)} inches")

# 5) Get the no of the dollars from the user apply the conversion of
# 1 dollar = 82 rupees and print the amount to the console in rupees
dollar_to_rupees=lambda c=int(input("no.of dollars")):c*82
print(dollar_to_rupees())

#
# 6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the
# string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"

source= lambda




#
# **************** Solutions provided in Solutions_Day01.py file **************
