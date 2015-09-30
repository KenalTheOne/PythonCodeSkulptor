def eval1(n):
    return (n % 10) / 10

def eval2(n):
    return ((n - n % 10) % 100) / 10

def eval3(n):
    return (n // 10) % 10

a = 654981
b = 123

print eval1(a)
print eval1(b)
print ""
print eval2(a)
print eval2(b)
print ""
print eval3(a)
print eval3(b)

def func(x):
    return -5*x**5 + 69*x**2 - 47

print func(0)
print func(1)
print func(2)
print func(3)

def future_value(present_value, annual_rate, periods_per_year, years):
    rate_per_period = annual_rate / periods_per_year
    periods = periods_per_year * years
    return present_value*(1+rate_per_period)**periods
    # Put your code here.

print "$1000 at 2% compounded daily for 3 years yields $", future_value(1000, .02, 365, 3)
print future_value(500, .04, 10, 10)

import math
def poly_square(n,s):
    return 1.0/4 * n * s**2 / math.tan(math.pi/n)

print poly_square(7,3)

def max_of_2(a, b):
    if a > b:
        return a
    else:
        return b

def max_of_3(a, b, c):
    return max_of_2(a, max_of_2(b, c))
########################
def project_to_distance(point_x, point_y, distance):
    dist_to_origin = math.sqrt(point_x ** 2 + point_y ** 2)    
    scale = distance / dist_to_origin
    return point_x * scale, point_y * scale
    
print project_to_distance(2, 7, 4)