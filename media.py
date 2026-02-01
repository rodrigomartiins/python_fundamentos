# --- Aplicação para calcular uma média entre diversas notas! ---
def calcular_media():
    '''Função para o calculo da média.'''
    try:
        quantidade = int (input('Quantas notas você gostaria de inserir? '))
        
        if quantidade <= 0:
            print('Erro: a quantidade deve ser maior que zero.')
        else:
            soma = 0
        
        for i in range(quantidade):
            nota = float (input(f'Digite a nota {i + 1} (0 a 10): '))
            if nota < 0 or nota > 10:
                print('Erro: nota inválida.')
                break
        
            soma += nota
        
        else:
                
            media = soma / quantidade
                
            if media <= 5 :
                print(f'A sua nota foi {media:.2f}, você está Reprovado!')
            elif media >= 5 and media < 7:
                print(f'A sua nota foi {media:.2f}, você está de Recuperação!')
            else:
                print(f'A sua nota final foi de {media:.2f}, parabéns você está Aprovado!')
# --- Neste segundo bloco é a função das medias para ter o resultado final. ---
            
    except ValueError:
        print('Erro: Digite apenas números')
# --- Aqui retorna a mensagem de erro caso o usuário não coloque números válidos para calcular a media.

while True:
    print('\n == MENU ==')
    print('1 . Calcular Média')
    print('2 . Sair')
    
    opcao = input('Escolha uma opção: ')
    
    if opcao == '1':
        calcular_media()
    elif opcao == '2':
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida! Tente novamente.')
    
