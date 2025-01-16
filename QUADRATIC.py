#using python to solve and draw quadractic equations


import cmath
import matplotlib.pyplot as plt 
import numpy as np

def solve_quadratic(a,b,c):
    #print("To find the roots of an equation")
    d = (b*b)
    e = (4*(a)*(c))
    discriminant =cmath.sqrt(d - e)
    root1 = (-b + discriminant)/ 2*(a)
    root2 = (-b - discriminant)/ 2*(a)
    #print(root1, root2)

    return root1, root2
#*********************************************
def findy(defx, defa, defb, defc):
    x2 = defx *defx
    return((defa * x2) + (defb * defx) + defc)
#8************************************************
def findy2(defx, defa, defb, defc, defd):
    x2 = defx * defx
    x3 = defx * defx * defx
    
    return((defa * x3)+(defb * x2) + (defc * defx) + defd), x3
#*************************************************
def dydx(defx, defa, defb, defc, defd):
    x2 = defx * defx
    x3 = defx * defx * defx
    return ((x3 * defa) * x2) + ((x2 * defb) * defx) + (defc * 1) + (defd * 0)
#*************************************************
def vertex(a, b, c):
    thevertex = ((-b**2)/4*a) + c
    print(thevertex)
    return thevertex

#############################################

a = int(input("cubic coefficient"))
b = int(input("quadratic coefficient"))
c = int(input("Linear coefficient"))
d = int(input("constant"))

vertex(a, b, c)
start = -0.050
stop =  0.050

x = np.arange(start, stop, 1/200)
y = dydx(x, a, b , c,d)


plt.subplot()
plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.show()
