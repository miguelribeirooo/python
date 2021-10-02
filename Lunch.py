x = input().split()
codigo = int(x[0])
qtd = int(x[1])

if(codigo == 1):
    total = qtd * float(4.00)
    print('Total: R$ %.2f'%total)

if(codigo == 2):
    total = qtd * float(4.50)
    print('Total: R$ %.2f'%total)

if(codigo == 3):
    total = qtd * float(5.00)
    print('Total: R$ %.2f'%total)

if(codigo == 4):
    total = qtd * float(2.00)
    print('Total: R$ %.2f'%total)

if(codigo == 5):
    total = qtd * float(1.50)
    print('Total: R$ %.2f'%total)       