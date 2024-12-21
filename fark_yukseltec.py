from math import *
 
v1 = 6.98
v2 = 7.0

r1 = 20000
rf = 40000

rload = 50000

vout = (rf / r1) * (v2 - v1)

print(vout, "V")

i0 = vout / rload

print(i0, "A")
print(i0 * 1000000, "micro amper")