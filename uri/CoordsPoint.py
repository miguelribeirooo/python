valor = input().split()
x, y = valor

x = float(x)
y = float(y)

if x == 0:
    if y == 0:
        print('Origem')
    if y != 0:
        print('Eixo Y')
elif y == 0:
    if x != 0:
        print('Eixo X')
elif x > 0:
    if y > 0:
        print('Q1')
    if y < 0:
        print('Q4')
elif x < 0:
    if y > 0:
        print('Q2')
    if y < 0:
        print('Q3')