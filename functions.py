# f(x) = 2x + 1
def f(x):
    return 2*x + 1

x_values = [0, 1, 2, 3]

for x in x_values:
    y = f(x)
    print(y)


# Charting a linear function in Python using SymPy
from sympy import *

x = symbols("x")
f = 2*x + 1
plot(f)


# Charting an exponential function
x = symbols("x")
f = x**2 + 1
plot(f)