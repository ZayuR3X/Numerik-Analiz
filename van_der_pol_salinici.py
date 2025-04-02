# Van der pol salınıcı
from numpy import *
from matplotlib.pyplot import *

def rk4m(x0, y0, h, n):
    x = x0
    y = y0
    xd = [x0]
    yd = [y0]
    for i in range(n + 1):
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        yd.append(y)
        x = x + h
        xd.append(x)
    return np.array(xd), np.array(yd)

def f(x,y):
    f = zeros((2))
    f[0] = y[1]
    f[1] = -y[0] + (1 - y[0]**2) * y[1]
    return f

h=0.3
n=198
t0=0.0 
y0= array([0.01,0.01])
T , Y = rk4m(t0,y0,h,n)
y1=[u1 for u1,u2 in Y]  
y2=[u2 for u1,u2 in Y]
for i in range(0,n):
    print(T[i],Y[i])

plot(y1,y2)
xlabel('y1')
ylabel('y2')
title('van der pol salınıcısı')
show()