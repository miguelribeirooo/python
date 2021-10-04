notas = input().split()

n1, n2, n3, n4 = notas

media = (float(n1) * 2 + float(n2) * 3 +float(n3) * 4 +float(n4) * 1) / 10

print('Media: %.1f'%media)

if(media >= 7):
    print('Aluno aprovado.')
elif(media < 5):
    print('Aluno reprovado.')

elif(5 <= media <= 6.9):
    print('Aluno em exame.')
    exame = float(input())
    print('Nota do exame: %.1f'%exame)
    mediafinal = (media + exame)/2
    if(mediafinal >= 5):
        print('Aluno aprovado.')
        print('Media final: %.1f'%mediafinal)
    elif(mediafinal > 5):
        print('Aluno reprovado.')
        print('Media final: %.1f'%mediafinal)

    