from modules.cadastro_func import menu as menu_cadastro
from modules.media_func import menu as menu_media

def menu_principal():
    while True:
        print('\n' + '='*25)
        print('    SISTEMA INTEGRADO v1.0')
        print('='*25)
        print('1 - Gerenciar Cadastros')
        print('2 - Cálcular Médias')
        print('3 - Sair')
        
        opcao = input('\nEscolha uma área do sistema: ').strip()
        
        if opcao == '1':
            menu_cadastro()
        elif opcao == '2':
            menu_media()
        elif opcao == '3':
            print('Encerrando o sistema...')
            break
        else:
            print('Opção Inválida!')
            
if __name__ == '__main__':
    menu_principal()
