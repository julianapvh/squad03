# def retornar_ao_menu_anterior(options):

#     return opcoes

# def mensagem_de_erro():
#     excecao = [OSError('Erro 1'), ('Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção...')]
#     raise ExceptionGroup('there were problems', excecao)
    
def menu_voltar_sair():
    while True:
        opcao_voltar_sair = int(input("\nDigite [1] para encerrar o atendimento ou [2] para voltar ao menu anterior: "))
        if opcao_voltar_sair == 1:
            print("Obrigado por usar nosso atendimento. Volte sempre!")
            exit()
        elif opcao_voltar_sair == 2:
            break
        else:
            print("Insira uma opção válida")


def sair():
    print("Obrigado por usar nosso atendimento. Volte sempre!")
    exit()