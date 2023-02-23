# 13. Given a string and a non-negative int n, return a string ouput that is n copies of the original string.


# string_multiplier('Hi', 2) → 'HiHi'
# string_multiplier('Hi', 3) → 'HiHiHi'
# string_multiplier('Hi', 1) → 'Hi'

def string_num(string,num):
    return string*num
string=input("Enter string eg Hi :")
num=int(input("Enter number :"))
res=string_num(string, num)
print(res)