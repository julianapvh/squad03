def menu_voltar_sair():
    while True:
        opcao_voltar_sair = input("\nDigite [1] para encerrar o atendimento ou [2] para voltar ao menu anterior: ")
        if opcao_voltar_sair == "1":
            print("Obrigado por usar nosso atendimento. Volte sempre!")
            exit()
        elif opcao_voltar_sair == "2":
            break
        else:
            print("Insira uma opção válida")


def sair(nome):
    print(f"Obrigado {nome} por usar nosso atendimento. Volte sempre!")
    exit()