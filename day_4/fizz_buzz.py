# d/v 3-> fizz
# d/v 5-> Buzz
#o/o   4 R %5 -> fizz buzz

###  prog for FIZZ BUZZ
num=int(input("Please enter a num : "))
skip=0
while (skip<num):
   if num%3==0:
    print("Fizz")
   elif num%5==0:
     print("Buzz")
   elif num%3==0 and num%5==0:
    print("Fizz Buzz")
   else:
     print("Invalid Input")

def  fizz_buzz(num):
    skip=1
while (skip):
    if num%3==0:
     print("Fizz")
     continue
    elif num%5==0:
     print("Buzz")
     continue
    elif num%3==0 and num%5==0:
     print("Fizz Buzz")
     continue
    else:
     print("Invalid input")
skip=int(input("Enter 1 for contiue and 0 for exit"))


ret_val=fizz_buzz(num)
print(ret_val)
y=input("Do you want to continue??")


# TEST CASES:

# 50: BUZZ
# 30: FIZZ BUZZ
# 9 : FIZZ
# 22 :: Invalid input


