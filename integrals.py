
# with oldway
def approximate_integral(a,b,n,f):
    delta_x = (b-a)/n
    total_sum = 0

    for i in range(1, n + 1):
        midpoint = 0.5 * (2 * a + delta_x * (2 * i - 1))
        total_sum += f(midpoint)
    
    return  total_sum * delta_x

def my_function(x):
    return x**2 + 1

area = approximate_integral(a=0, b=1, n=5, f=my_function)

print(area)

# if we use 1000 rectangles
area = approximate_integral(a=0, b=1, n=1000, f=my_function)

print(area)


from sympy import *

# declare 'x' to sympy
x = symbols('x')

# now just use python syntax to declare function
f = x**2 + 1

# calculate the integral of the function with respect to x
# for the area between x = 0 and 1
area = integrate(f, (x, 0, 1))

print(float(area))


# using limits to calculate integrals

# declare variables to sympy
x, i, n = symbols('x i n')

# declare function and range
f = x**2 + 1
lower, upper = 0, 1

# calculate width and each rectangle height at index "i"
delta_x = ((upper - lower) / n)
x_i = (lower + delta_x * i)
fx_i = f.subs(x, x_i)

# iterate all "n" rectangles and sum their areas
n_rectangles = Sum(delta_x * fx_i, (i, 1, n)).doit()

# calculate the area by approaching the number
# of rectangles "n" to infinity
area = limit(n_rectangles, n, oo)

print(area)