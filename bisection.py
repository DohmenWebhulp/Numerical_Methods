import numpy as np

def bisect(a, b, f, tol, max_iter = 100):
    i = 0
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

def newton(p_n, f, df, tol, max_iter):
    if(df(p_n) < 1e-2):
        return ValueError 
    i = 0
    while(i < max_iter):
        p = p_n - (f(p_n)/df(p_n))
        if(abs(p - p_n) < tol and abs(f(p)/df(p)) < tol):
            print(f"Number of steps = {i + 1}")
            break
        p_n = p
        print(p)
        i += 1
    return p

def f(x):
    return x - np.cos(x)

def df(x):
    return 1 + np.sin(x)

def g(x):
    return 4/(x * x + 3)
    
tol = pow(10, -2)
max_iter = 100

while(True):
    method = input("Which method would you like to try? ([B/N/P]): ")
    if(method == 'B' or method == 'N' or method == 'P'):
        if(method == 'B'):
            a = float(input("Give us the left of the interval: "))
            b = float(input("Give us the right of the interval: "))
            root = bisect(a, b, f, tol, max_iter)
            print(root)
        if(method == 'N'):
            p_0 = float(input("Give us the initial value: "))
            root = newton(p_0, f, df, tol, max_iter)
            print(root)
        if(method == 'P'):
            p_0 = float(input("Give us the initial value: "))
            root = picard(p_0, g, tol, max_iter)
            print(root)
    else:
        print("Try Again!")