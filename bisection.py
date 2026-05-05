import numpy as np
from decimal import Decimal
#The Bisection algorithm halves the interval in which a function f(x) = 0, with a < x < b.
def bisect(a, b, f, tol, max_iter = 100):
    i = 0
    #the function should change sign over the interval
    if(f(a) * f(b) > 0):
        return ValueError
    while(i < max_iter):
        p = (a + b)/2
        if(abs(f(p)) < tol):
            print(f"Number of steps = {i + 1}")
            break
        if((f(a) * f(p) < 0)):
            b = p
        else:
            a = p
        i += 1
        print(p)
    return p

#The Picard algorithm iteratively calculates p_n+1 as a result of the fixed point iteration p_n+1 = g(p_n)
def picard(p_n, g, tol, max_iter):
    i = 0
    while(i < max_iter):
        p = g(p_n)
        if(abs(p - p_n) < tol):
            print(f"Number of steps = {i + 1}")
            break
        p_n = p
        print(p)
        i += 1
    return p

#The newton algorithm calculates the new value p as the old value minus the tangent there.
def newton(p_n, a, f, df, tol, max_iter):
    #The derivative should not be too small, as the algorithm will yield unstable results.
    if(df(p_n) < 1e-2):
        return ValueError 
    i = 0
    a = Decimal(a)
    while(i < max_iter):
        p = p_n - (f(p_n, a)/df(p_n))
        if(abs(p - p_n) < tol and abs(f(p, a)/df(p)) < tol):
            print(f"Number of steps = {i + 1}")
            break
        p_n = p
        print(p)
        i += 1
    return p

def f(x, a):
    return x*x - a

def df(x):
    return 2*x

#fixed-point method
def g(x):
    return 4/(x * x + 3)
    
tol = pow(10, -12)
max_iter = 100
"""
while(True):
    #The user can choose which algorithm to use
    method = input("Which method would you like to try? ([B/N/P]): ")
    if(method == 'B' or method == 'N' or method == 'P'):
        if(method == 'B'):
            #The user can choose the interval in which to apply Bisection
            a = float(input("Give us the left of the interval: "))
            b = float(input("Give us the right of the interval: "))
            root = bisect(a, b, f, tol, max_iter)
            print(np.decimal(root))
        if(method == 'N'):
            #The user can choose the initial value
            a = float(input("Give us the targeted root: "))
            root = newton(1, a, f, df, tol, max_iter)
            print(np.decimal(root))
        if(method == 'P'):
            #The user can choose the initial value
            p_0 = float(input("Give us the initial value: "))
            root = picard(p_0, g, tol, max_iter)
            print(root)
    else:
        print("Try Again!")
"""
root_2 = newton(1, 2, f, df, tol, max_iter)
root_3 = newton(1, 3, f, df, tol, max_iter)
root_5 = newton(1, 5, f, df, tol, max_iter)