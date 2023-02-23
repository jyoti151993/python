# SWAP of two nos
# to take the inputs from the user 

x=input('Enter the value of x: ')
y=input('Enter the value of y: ')

#create a temporary variable  and swap the value
temp=x
x=y
y=temp

print('The value of x after swapping {}'.format(x))
print('The value of y after swapping {}'.format(y))