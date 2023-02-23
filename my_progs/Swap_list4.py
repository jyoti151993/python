# python prog to swap first and last elemnt

# swap function
def swapList(list):
    start, *middle, last=list
    list=last, *middle, start
    return list


list=[24,45,35,67]
print(swapList(list))    