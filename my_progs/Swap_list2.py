# python prog to swap first and last element of a list


# swap function
def swapList(newList):
     newList[0],newList[-1]=newList[-1],newList[0]

     return newList

newList=[12,35,24,55]

print(swapList(newList))