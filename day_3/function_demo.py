
print("I am printing some value")

# function without a return statement
def my_functionname():
    print("I am printing some value")

    return_val= my_function()
    print("Returned value from the function is ",return_val)

# function with a return statement
    def my_functionname():
        print("I am printing some value")
        return 1
    return_val= my_function()
    print("Returned value from the function is ",return_val)

# addition function
def my_addition_function(num1=11, num2=10, num3=90):
    return num1+num2+num3


return_val=my_addition_function(11,10,100)
print("Returned value from my_addition_function is ",return_val)


# addition function
def my_addition_function(num1=11, num2=10, num3=90):
    return num1+num2+num3


return_val=my_addition_function(11,num2=20,100) # throws an error 
print("Returned value from my_addition_function is ",return_val)