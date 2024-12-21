from math import *

# Aralığı yarıya bölerek kök bulma

def yarila (a,b,tol):
    if f(a)*f(b) > 0.0:
        print("Bu aralıkta kök yok")
    else:
        dx = b - a
        while(abs(dx>tol)):
            xm = (a+b)/2
            if(f(a)*f(xm) < 0.0):
                b = xm
                dx = b - a
            else:
                a = xm
                dx = b - a
    return xm

def f(x):
    return exp(x)*log(x)-x*x

a = 1.0
b = 3.0
tol = 1.0e-8
print("X = " "%.11f" % yarila(a,b,tol))