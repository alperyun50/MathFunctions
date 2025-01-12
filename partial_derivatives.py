from sympy import *
from sympy.plotting import plot3d

# declare x and y to sympy
x,y = symbols('x y')

# now just use python syntax to declare function
f = 2*x**3 + 3*y**3

# calculate the partial derivatives for x and y
dx_f = diff(f, x)
dy_f = diff(f, y)

print(dx_f)
print(dy_f)

# So for (x,y) values (1,2), the slope with respect to x is 6(1) = 6 
# and the slope with respect to y is 9(2)*2 = 36.

# plot the function
# plot3d(f)


# using limits to calculate a slope
# "x" and step size "s"
x, s = symbols('x s')

# declare functions
f = x**2

# slope between two points with gap "s"
# substitute into rise-over-run formula
slope_f = (f.subs(x, x + s) - f) / ((x + s) - x)

# substitute 2 for x 
slope_2 = slope_f.subs(x, 2)

# calculate slope at x = 2
# infinitely approach step size _s_ to 0
result = limit(slope_f, s, 0)

print(result)

# Using limits to calculate a derivative
# "x" and step size "s"
x,s = symbols("x s")

# declare function
f = x**2

# slope between two points with gap "s"
# substitude into rise over run formula
slope_f = (f.subs(x, x + s) - f) / ((x+s) - x)

# calculate derivative function
# infinitely approach step size +s+ to 0
result = limit(slope_f, s, 0)

print(result) 


# z = (x**2 + 1)**3 − 2 
# find the derivative of z

z = (x**2 + 1)**3 - 2
dz_dx = diff(z,x)
print(dz_dx)