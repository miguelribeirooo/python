x = input().split()
a, b, c =x

a = float(a)
b = float(b)
c = float(c)
n1 = float(1)
n2 = float(1)
n3 = float(1)

if a >= b and a >= c:
    a = n1
    if b >= c:
        b = n2
        c = n3
    else:
        c = n2
        b = n3
if b >= a and b >= c:
    b = n1
    if a >= c:
        a = n2
        c = n3
    else:
        c = n2
        a = n2

if c >= a and c >= b:
    c = n1
    if a >= b:
        a = n2
        b = n3
    else:
        b = n2
        a = n3

if a == b and b == c:
    n1=a
    n2=b
    n3=c

a = n1
b = n2
c = n3

if a >= (b+c):
    print('NAO FORMA TRIANGULO')
else:
    if(a ** 2) == (b ** 2 + c ** 2):
        print('TRIANGULO RETANGULO')
    if(a ** 2) > (b ** 2 + c ** 2):
        print('TRIANGULO OBTUSANGULO')
    if(a ** 2) < (b ** 2 + c ** 2):
        print('TRIANGULO ACUTANGULO')
    if(a == b == c):
        print('TRIANGULO EQUILATERO')
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')