from math import *

print("Gerçek değeri: " , cos(1))

print("-----------------------------")



def f(x):
    return sin(x)
a=1.0 
h=0.1
for i in range(14):
    fl=(f(a+h)-f(a))/h
    print ('%.12f' % h,'%.10f'% \
          fl,'%.10f' % float(cos(a)-fl))
    h=h/10.0