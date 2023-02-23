    # python program to swap first and last element of the list

# Swap function
def swapList(newList):
        size=len(newList)

    # swapping 
        temp=newList[0]
        newList[0]=newList[size-1]
        newList[size-1]=temp
     
        return newList


newList=[12,35,9,56,44]
print(swapList(newList))