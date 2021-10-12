x = float(input())

if x <= 400.00:
    salario = x * 1.15
    reajuste= salario - x
    percentual= 15
if 400.01 <= x <= 800.00:
    salario = x * 1.12
    reajuste= salario - x
    percentual= 12
if 800.01 <= x <= 1200.00:
    salario = x * 1.10
    reajuste= salario - x
    percentual= 10
if 1200.01 <= x <= 2000.00:
    salario = x * 1.07
    reajuste= salario - x
    percentual= 7
if  x > 2000.00:
    salario = x * 1.04
    reajuste= salario - x
    percentual= 4

print('Novo salario: {:.2f}'.format(salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))