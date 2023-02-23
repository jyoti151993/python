#  Write a Python program to find the item with maximum frequency in a given list. 

# Sample :
# Original list:
# [2, 3, 8, 4, 7, 9, 8, 2, 6, 5, 1, 6, 1, 2, 3, 2, 4, 6, 9, 1, 2]
# Item with maximum frequency of the said list:
# (2, 5)

from statistics import mode
test_l=[ int(x) for x in input("input the comma separated numbers : ").split(",")]
def maxim_freq(test_l):
    res= mode(test_l)
    return res

print(maxim_freq(test_l))
# print("Original List : ",test_l)
# dict={ x:test_l.count(x) for x in test_l}
# print(dict)
           
# d={}
# for items in test_l:
#     d[items]= d.get(items,0)+1
# print(d)    


# def freq_dist(test_l):
#     return {i:test_l.count(i) for i in test_l}   

# print(freq_dist(test_l))