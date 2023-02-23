    
# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
    # storing the first and last elemt as a tuple
    get=list[-1],list[0]
 # unpacking the tuple elements
    list[0],list[-1] =get

    return list

 # driver code
list=[13,24,35,44]
print(swapList(list))

