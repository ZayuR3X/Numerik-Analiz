from math import *

def f(x):
    return tan(x)

def f1(x):
    return 1. / (cos(x)**2)

h = 0.001

for i in range (3):
    x = float(i+1)
    #f1_ileri = (f(x+h) - f(x)) / h - f1(x)
    #f1_geri = (f(x) - f(x-h)) / h - f1(x)
    f1_merkez = (f(x+h) - f(x-h)) / (2*h) - f1(x)
    f1_tam = f1(x)
    f1_m2 = (f(x-2*h) - 8*f(x-h) + 8*f(x+h) - f(x+2*h)) / (12*h) - f1(x) # iki nokta ileri ve iki nokta geri
    print ("%.10f" % f1_merkez, "%.10f" % f1_m2)
