def retornar_ao_menu_anterior(options):

    return opcoes

def mensagem_de_erro():
    excecao = [OSError('Erro 1'), ('Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção...')]
    raise ExceptionGroup('there were problems', excecao)
    
    


