#FUNÇÃO PARA COLOCAR '=' E CRIAR SEPARAÇÃO NO TEXTO
def linhas():
    print("-=" * 10)
    #FUNÇÃO COM O NOME DA LOJA OU DO CHATBOT
def chatbot(nome='Chat Bot'):
    
    nome_cliente = str(input("Olá! Seja Bem Vindo(a) a Loja Store!!! Como Gostaria de Ser Chamado(a)? "))
    
    linhas()
    print('Agora que já sei seu nome ' + str(nome_cliente) + ' Vamos prosseguir com seu atendimento! ')
    
    linhas()
    print(nome_cliente + str(' Agora vou te mostrar as opções!'))
    linhas()
    
    #LOOP DE OPÇÕES
    while True:
        
        print("""
        OPÇÕES: ESCOLHA UMA:
        [1] - Ver Produtos
        [2] - Ver Promoções
        [3] - Preço dos Produtos
        [4] - Falar com Atendente
        [5] - Encerrar Conversa
        """)
        #VARIAVEIS DE LISTAS COM OS PRODUTOS E PREÇOS
        escolha = str(input("Escolha uma opção de 1 a 5: ")).lower().strip()
        produtos = ["produto1", "produto2", "produto3", "produto4", "produto5"]
        promocoes = ["produto1", "produto5"]
        precoProduto = [10.99, 5.99, 6.99, 8.50, 4.60]
        atendente = "Olá, eu me chamo CHAT BOT, e vou dar sequencia ao seu atendimento."
        #CONDIÇÕES
        if escolha == "1":
            linhas()
            for item in produtos:
                print(item)
            linhas()
        elif escolha == "2":
            linhas()
            for item in promocoes:
                print(item)
            linhas()
        elif escolha == "3":
            linhas()
            for item in precoProduto:
                print(item)
            linhas()
        elif escolha == "4":
            linhas()
            print(atendente)
            linhas()
        elif escolha == "5": 
            break
        else:
            print("Opção inválida, tente novamente!")
            continue
  
chatbot("")
print("Obrigado pela preferência, volte sempre!!!")


