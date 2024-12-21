from math import *

# Kiriş yöntemi ile kök bulma

def kiris(a,b,tol):
    x0 = a 
    x1 = b 
    dx = b - a
    iter = 1
    while(abs(dx) > tol):
        x2 = x1 - (x1 - x0) * f(x1) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        dx = x1 - x0
        if iter > 50:
            print("50 iterasyon kök bulunamadı!")
            return x2
        iter += 1
    return x2

def f(x):
    return exp(x) * log(x) - x**2

a = 3.0
b = 5.0
tol = 1.0e-8
x = kiris(a,b,tol)
print("X = " "%.11f" % x)