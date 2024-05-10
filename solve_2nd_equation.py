
"""
solve a 2nd degree equation
"""
def DELTA(a,b,c):
    delta =b**2 - (4*a*c) 
    print(delta)
    return(delta)
import math
a = int(input ("please enter a:"))
b = int(input ("please enter b:"))
c = int(input ("please enter c:"))
x = DELTA(a,b,c)
d = math.sqrt(abs(x))
print(d)
x1 = (-b+d)/(2*a)
x2 = (-b-d)/(2*a)
print("x1=",x1 , "," ,"x2=",x2)