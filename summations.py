# 5
# Σ 2i = (2)1 + (2)2 + (2)3 + (2)4 + (2)5 = 30
#i=1

summation = sum(2*i for i in range(1,6))
print(summation)


x = [1,4,6,2]
n = len(x)

summation = sum(10*x[i] for i in range(0,n))
print(summation)


from sympy import *

i,n = symbols("i,n")

# iterate each element i from 1 to n,
# then multiply and sum
summation = Sum(2*i,(i,1,n))

# specify n as 5,
# iterating the numbers 1 through 5
up_to_5 = summation.subs(n, 5)
print(up_to_5.doit()) # 30



