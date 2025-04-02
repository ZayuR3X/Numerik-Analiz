# Sürtünmeli atış hareketi

from numpy import *
from pylab import *

def rk4m(x0,y0,h,n):
    x = x0 ; y = y0; xd = [x0]; yd = [y0]
    for i in range(n+1):
        k1 = h * f(x,y)
        k2 = h * f(x + h/2, y + k1/2)
        k3 = h * f(x + h/2, y + k2/2)
        k4 = h * f(x + h, y + k3)
        y = y + (k1 + 2*k2 + 2*k3 + k4)/6
        yd.append(y)
        x = x + h
        xd.append(x)
    return xd, yd
    
def f(x,y):
    f = zeros((4))
    f[0] =  y[2]
    f[1] =  y[3]
    f[2] = -0.01*y[2]*sqrt(y[2]**2 + y[3]**2)
    f[3] = -0.01*y[3]*sqrt(y[2]**2 + y[3]**2) - 9.8
    return f

h = 0.01
n = 180
t0 = 0.0
y0 = array([0.0, 0.0, 6.0, 8.0])

T,Y = rk4m(t0, y0, h, n)

x = [y1 for y1, y2, y3, y4 in Y]
y = [z2 for z1, z2, z3, z4 in Y]

y_tam = (y0[2] / y0[3] - 5*(array(x)/y0[2]**2))*array(x)

for i in range(n):
    print("%10.3f" % x[i], "%12.3f" % y[i], "%12.3f" % y_tam[i])

scatter(x, y)
scatter(x, y_tam)
xlim(0.0, 10.0)
ylim(-3.0, 4.0)
show()