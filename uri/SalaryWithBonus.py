import math

valor = input().split(" ")

a, b, c = valor

maior = (int(a) + int(b) + abs(int(a) - int(b)))  / 2
resultado = (int(maior) + int(c) + abs(int(maior) - int(c)))/2

print("%d eh o maior" %resultado)

[a, b, c] = input().split(' ')
a = int(a)
b = int(b)
c = int(c)

maior = max(a, b, c)
print(maior)