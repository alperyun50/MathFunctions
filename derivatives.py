def derivative_x(f, x, step_size):
    m = (f(x + step_size) - f(x)) / ((x + step_size) - x)
    return m

def my_function(x):
    return x**2

slope_at_2 = derivative_x(my_function, 2, .00001)

print(slope_at_2)


# calculating derivatives with sympy
from sympy import *

# declare 'x' to sympy
x = symbols('x')

# now just use python syntax to delare function
f = x**2

# calculate the derivatives of the fonction
dx_f = diff(f)
print(dx_f)

def dx_f(x):
    return 2*x

slope_at_2 = dx_f(2.0)

print(slope_at_2)

# calculate slope at x = 2
print(dx_f.subs(x,2)) 