from pylab import *
from math import *

# Ising Modeli 
def newton(a,tol):
    x1 = a 
    x = x1 - f(x1) / f1(x1)
    iter = 1
    while(iter<=50):
        while(abs(x-x1)>tol):
            x1 = x
            x = x1 - f(x1) / f1(x1)
        if iter > 50:
            print("50 itersayon kök yok")
            return x
        iter += 1
    return x

def f(x):
    global tdum
    return x - tanh(4.0*x/tdum)

def f1(x):
    global tdum
    return 1.0 - (4.0/tdum)/cosh(4*x/tdum)**2

nmax = 36
tmax = 7.0 
dt = tmax / nmax
tol = 1.0e-6

t = empty(nmax,float)
s = empty(nmax,float)

for i in range(nmax):
    tdum = (i+1) * dt
    s[i] = newton(tmax,tol)
    t[i] = tdum
    print ("t = " "%.3f" %t[i], "s = " "%.3f" %s[i])

plot(t,s,"g--")
plot(t,s,"kx")
ylim(-0.1,1.1)
xlabel("T")
ylabel("M")
show()