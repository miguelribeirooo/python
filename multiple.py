valor = input().split()
a, b = valor
a = int(a)
b = int(b)

if a > b:
    if a % b == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a < b:
    if b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')

if a == b:
    print('Sao Multiplos')