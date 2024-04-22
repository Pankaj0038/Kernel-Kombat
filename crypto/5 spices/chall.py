from Crypto.Util.number import getPrime, bytes_to_long

with open('flag.txt', 'rb') as f:
    flag = f.read()


n1 = getPrime(512)*getPrime(512)
n2 = getPrime(512)*getPrime(512)
n3 = getPrime(512)*getPrime(512)
n4 = getPrime(512)*getPrime(512)
n5 = getPrime(512)*getPrime(512)

e=3

m = bytes_to_long(flag)

c1 = pow(m,e,n1)
c2 = pow(m,e,n2)
c3 = pow(m,e,n3)
c4 = pow(m,e,n4)
c5 = pow(m,e,n5)
    
with open('encrypted-messages.txt', 'w') as f:
    f.write(f'n1= {n1}\n')
    f.write(f'e= {e}\n')
    f.write(f'c1= {c1}\n\n')
    f.write(f'n2= {n2}\n')
    f.write(f'e= {e}\n')
    f.write(f'c2= {c2}\n\n')
    f.write(f'n3= {n3}\n')
    f.write(f'e= {e}\n')
    f.write(f'c3= {c3}\n')
    f.write(f'n4= {n4}\n')
    f.write(f'e= {e}\n')
    f.write(f'c4= {c4}\n')
    f.write(f'n5= {n5}\n')
    f.write(f'e= {e}\n')
    f.write(f'c5= {c5}\n')
