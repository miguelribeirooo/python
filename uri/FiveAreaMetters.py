a = float(input())
b = float(input())
c = float(input())

pi = 3.14
areaTR = float((a * c)/2)
areaCIRC = float(pi * (c * c))
areaTRAP = float(((a + b) * c)/2)
areaQUAD = float(b * b)
areaRET = float(a * b)

print('TRIANGULO: {:.3f}'.format(areaTR))
print('CIRCULO: {:.3f}'.format(areaCIRC))
print('TRAPEZIO: {:.3f}'.format(areaTRAP))
print('QUADRADO: {:.3f}'.format(areaQUAD))
print('RETANGULO: {:.3f}'.format(areaRET))