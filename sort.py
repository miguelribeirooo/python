valor = input().split()
n1, n2, n3 = valor
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if(n1 > n2 and n1 > n3):
    d = n1
    if(n2 > n3):
        e = n2
        f = n3
    else:
        e = n3
        f = n2
if(n2 > n1 and n2 > n3):
    d = n2
    if(n1 > n3):
        e = n1
        f = n3
    else:
        e = n3
        f = n1
if(n3 > n1 and n3 > n2):
    d = n3
    if(n1 > n2):
        e = n1
        f = n2
    else:
        e = n2
        f = n1

print(f)
print(e)
print(d)
print()
print(n1)
print(n2)
print(n3)