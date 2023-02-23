# different types of tuples

# Empty_tuple
my_tuple = ()
print(my_tuple)

# tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [1, 2, 3], (8, 4, 6))
print(my_tuple)

""" A tuple can also be created without  using parenthesis. This is known as tuple packing"""

my_tuple = 3, 4.6, "dog"
print(my_tuple)

# tuple unpacking is also possible
a, b, c = my_tuple
print(a)
print(b)
print(c)

my_tuple = ("Hello")
print(type(my_tuple))  # <Class String>

# creating a tuple having just one  element
my_tuple = ("Hello",)
print(my_tuple)
print(type(my_tuple))

my_tuple = "Hello",
print(type(my_tuple))

# accessing the elements of the tuples
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[0]) # 'p'
print(my_tuple[5]) # '5'

# Index Error : tuple  Index out of range
# print(my_tuple[6])

# nested tuple
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

# nested index
print(n_tuple[0][3])  # s
print(n_tuple[1][1])  # 4
print(n_tuple[2][2])  # 3

# Negative indexing
my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
print(my_tuple[-1])  # t
print(my_tuple[-6])  # p


# slicing
# Accessing the tuple using slicing operator
my_tuple = ('P', 'r', 'o', 'g', 'r', 'm', 'i',' z')

# element 2nd to 4th
# output : ('r', 'o', 'g')
print(my_tuple[1:4])

# elems beginning to second
# output ('p','r')
print(my_tuple[:2])
print(my_tuple[:])

# elements from 8th to end
print(my_tuple[6:])

# elems beginning to second
print(my_tuple[:-7])