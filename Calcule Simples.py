def lista():
    print('-' * 34)
    print('            PRODUTOS')
    print('-' * 34)
    print('1 - 1L Leite Integral  - RS5,30')
    print('2 - 1KG Açúcar         - RS5,10')
    print('-' * 34)

def caixa():
    quantidade1 = int(input('-> Leite   Quantidade desejada: '))
    valor1 = quantidade1 * leite
    quantidade2 = int(input('-> Açúcar  Quantidade desejada: '))
    valor2 = quantidade2 * acucar
    total = valor1 + valor2
    print('-' * 34)
    print('TOTAL                  R${:.2f}'.format(total))
    print('-' * 34)

leite = 15.30
acucar = 5.20

lista()
caixa()
