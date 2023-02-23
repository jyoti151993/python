
# Python3 program to swap elements
# at given positions

# Swap function

def swapPositions(list, pos1,pos2):

    list[pos1],list[pos2]=list[pos2],list [pos1]
    return list


# Driver function

list=[24,45,89,56]
pos1, pos2=1,3
print(swapPositions(list,pos1-1,pos2-1))
