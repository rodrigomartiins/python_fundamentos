# --- Aplicação para calcular uma média entre notas! ---

def solicitar_quantidade_notas():
    while True:
        try:
            quantidade = int(input('Digite quantas notas gostaria de inserir: '))
            if quantidade > 0:
                return quantidade
            print('Erro: Digite um número maior que zero.')
        except ValueError:
            print('Erro: Digite um número inteiro válido.')

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

def processar_media(lista_notas):
    soma = sum(lista_notas)
    return soma / len(lista_notas)

def exibir_resultado(media):
    status = ""
    if media <= 5:
        status = 'Reprovado'
    elif media < 7:
        status = 'de Recuperação'
    else:
        status = 'Aprovado'
    print(f'\nSua média final foi de {media:.2f}. Status: {status}')

def executar_calculo():
    quantidade = solicitar_quantidade_notas()
    notas = []
    
    for i in range(1, quantidade + 1):
        nota_atual = solicitar_nota(i)
        notas.append(nota_atual)
        
    resultado = processar_media(notas)
    
    exibir_resultado(resultado)
    
def menu():
    '''Função que exibe o menu com as opções.'''
    while True:
        print('\n=== MENU ===')
        print('1 - Calcular média')
        print('2 - Sair')

        opcao = input('Escolha uma opção: ').strip()

        if opcao == '1':
           executar_calculo()
        elif opcao == '2':
            print('Saindo do programa...')
            break
        else:
            print('Opção Inválida')

if __name__ == "__main__":
    menu()
