# solving the  quadratic eqn
# solve the quadratic eqn ax**2+bx+c=0

#import complex math module
import cmath
a=1
b=5
c=6
# calculate the discriminant
d=(b**2)-(4*a*c)
# find the two solutions
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)

# display the solutions
print("The solutions are {0} and {1}".format(sol1,sol2))
