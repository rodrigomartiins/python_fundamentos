#Aplicação para calcular uma média entre duas notas!
try:    
    nota_1 = float (input('Digite a primeira nota (0/10):  '))
    nota_2 = float (input('Digite a segunda nota (0/10): '))
    
    if nota_1 < 0 or nota_1 > 10 or nota_2 < 0 or nota_2 > 10:
        print('Erro: As notas devem ser entre 0 e 10.')
    else: 
        media = (nota_1 + nota_2) / 2
    #Neste primeiro bloco nós isolamos a condição para que o usuário coloque os dados corretos para não quebrar a aplicação.
        
        if media <= 5 :
            print(f'A sua nota foi {media:.2f}, você está Reprovado!')
        elif media >= 5 and media < 7:
            print(f'A sua nota foi {media:.2f}, você está de Recuperação!')
        else:
            print(f'A sua nota final foi de {media:.2f}, parabéns você está Aprovado!')
        #Neste segundo bloco é a função das medias para ter o resultado final.
        
except ValueError:
    print('Erro: Digite apenas números')
    #Aqui retorna a mensagem de erro caso o usuário não coloque números válidos para calcular a media.
