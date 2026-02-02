# --- Aplicação para calcular uma média entre diversas notas! ---

def solicitar_quantidade_notas():
    '''Função para solicitar quantidade de notas.'''
    quantidade = int(input('Digite quantas notas gostaria de inserir: '))
    if quantidade <= 0:
        raise ValueError('Quantidade inválida!')
    return quantidade


def solicitar_nota(indice):
    '''Função que solicita a nota pro usuário.'''
    while True:
        try:
            nota = float(input(f'Digite a nota {indice} (0 a 10): '))
            if 0 <= nota <= 10:
                return nota
            else:
                print('Nota inválida. Digite um valor entre 0 e 10.')
        except ValueError:
            print('Digite apenas números.')


def calcular_media():
    '''Função para o calculo da média.'''
    try:
        quantidade = solicitar_quantidade_notas()
        soma = 0

        for i in range(1, quantidade + 1):
            soma += solicitar_nota(i)

        media = soma / quantidade
        exibir_resultado(media)
    except ValueError as erro:
        print(f'Erro: {erro}')


def exibir_resultado(media):
    '''Função que exibe o resultado da média.'''
    if media <= 5:
        print(f'Sua média final foi de {media:.2f}. Você está Reprovado.')
    elif media < 7:
        print(f'Sua média final foi de {media:.2f}. Você está de Recuperação.')
    else:
        print(f'Sua média final foi de {media:.2f}. Você foi Aprovado!')


def menu():
    '''Função que exibe o menu com as opções.'''
    while True:
        print('\n=== MENU ===')
        print('1 - Calcular média')
        print('2 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            calcular_media()
        elif opcao == '2':
            print('Saindo do programa...')
            break
        else:
            print('Opção Inválida')


if __name__ == "__main__":
    menu()
