
"""
Loops and Conditionals 
----------------------
# Solve the following using either while/do while loops
1) Take a number from the user and print sum from 1 to that number 
2) Take a number from the user and print all prime numbers from 1 to that number 
3) Take a number from the user and print all Odd numbers from 1 to that number 
4) Take a number from the user and print all Even numbers from 1 to that number 
5) Take a number from the user and print fibonacci sequence till that number
	eg : fibonnaci sequence for 5 is 0,1,1,2,3,5

"""
# solution 1\
num = int(input("Enter a number:::"))
sum = 0
for i in range(num+1):
    sum += i
print(sum)

# solution 2
flag =False
if num>1:
   # check for the factors
   for i in range(2 , num+1):
      if (num%i)==0:
        # if factor is found set flag to true
        flag=True
        break


if flag:
    print(num, "is a prime number")
else :
    print(num, "not a prime no.")


#solution 3,4

for i in range(1, num+1):
    if (i%2) == 0:
        print(i,"is a even no")
    elif i%2==1:
        print(i ,"is a odd no")

#solution 5

# Program to display the Fibonacci sequence of the nth term
nterms=int(input("How many terms? "))

# first two terms
i, j =0,1
count=0
sum =0
# check if the number of term is valid
if nterms<=0:
    print(0)
    # if there is only one term , return n1

else:

     print("Fibonacci Sequence")
     while i<=nterms:
            
            print(i)
            sum=i+j
            # update values
            i=j
            j=sum


