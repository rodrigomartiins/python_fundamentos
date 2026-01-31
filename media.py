#Aplicação para calcular uma média entre duas notas!

nota_1 = float (input('Digite a primeira nota: '))
nota_2 = float (input('Digite a segunda nota: '))
media = (nota_1 + nota_2) / 2

if media <= 5 :
    print(f'A sua nota foi {media:.2f}, você está Reprovado!')
elif media > 5 and media <= 7:
    print(f'A sua nota foi {media:.2f}, você está de Recuperação!')
else:
    print(f'A sua nota final foi de {media:.2f}, parabéns você está Aprovado!')
