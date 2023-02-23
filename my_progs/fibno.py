# Program to display the Fibonacci sequence of the nth trem
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
        
    