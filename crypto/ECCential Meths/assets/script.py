from Crypto.Util.number import *

a = -228
b = 848
p = 9739

def add_point(p1, p2):
    if p1 == (0,0):
        return p2
    if p2 == (0,0):
        return p1
    
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2 and y1 == -y2:
        return (0, 0)

    lamda = 0
    if p1 == p2:
        lamda = ((3*pow(x1,2,p)+a) * inverse(2*y1, p))
    else:
        lamda = ((y2-y1) * inverse(x2-x1, p))
        
    x3 = (pow(lamda, 2) - x1 - x2) % p
    y3 = (lamda*(x1 - x3) - y1) % p 
    return (x3, y3)


def multi(P,n):
    if n==0:
       return (0,0)
    elif n==1:
       return P
    elif n%2 == 1:
       return add_point(P, multi(P, n-1))
    else: 
       return multi(add_point(P,P), n/2)
       

A = (94, 900)
n = 1337

C = A

B = multi(C,n)
print(B)
