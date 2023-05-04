from funcoes import *


print("Olá! Seja Bem vindo a loja SQUAD 3\n")
nome = input("Como você gostaria de ser chamado(a)? ").title()

#LOOP PRINCIPAL
while True:
    #MENU PRINCIPAL 
    opcoes = input(
        f"\n{nome}, em que podemos te ajudar?\n"
        "[1] Entregas\n"
        "[2] Pedidos e Pagamentos\n"
        "[3] Trocas e Devolução\n"
        "[4] Produtos\n"
        "[5] Cadastro\n"
        "[6] Encerrar Atendimento\n"
        "Insira o número do atendimento que deseja: "
    )
    
    if opcoes == "1": #ENTRA NO LOOP OPÇÃO ENTREGAS
        while True:
            opcao_entregas = input(
                "\nQual a sua dúvida sobre entregas: \n"
                "[1] Como rastrear meu pedido?\n"
                "[2] Qual o prazo de entrega do meu pedido?\n"
                "[3] Como alterar meu endereço de entrega?\n\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_entregas == "1": #COMO RASTREAR PEDIDO
                print("\nDentro de “Minha conta” clique em “Meus pedidos” e procure pela sua comprinha. Elas estão organizadas pelo número de identificação. Para ver mais detalhes clique em VER DETALHES. O código de rastreio deve aparecer logo abaixo do resumo da sua compra. Mas lembre-se que ele aparece de formas diferentes dependendo da forma de entrega que você selecionou. Com o código de rastreio em mãos, basta você localizar a sua comprinha no site dos Correios.")
                menu_voltar_sair()
            elif opcao_entregas == "2": #PRAZO DE ENTREGA
                print("\nO prazo de entrega vai depender do seu estado.")
                menu_voltar_sair()
            elif opcao_entregas == "3": #ALTERAR ENDEREÇO DE ENTREGA
                print("\nOs Correios não permitem que a gente altere nenhuma informação após o despacho da sua comprinha. Por isso, vamos ter que aguardar a sua comprinha retornar para a nossa loja para um novo despacho.")
                menu_voltar_sair()
            elif opcao_entregas == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_entregas == "5": #VOLTAR AO MENU ANTERIOR
                break
            else: 
                print("Por favor, insira uma opção válida: ")
                
    elif opcoes == "2": #ENTRA NO LOOP PEDIDOS E PAGAMENTOS
        while True:
            opcao_pedidos_pagamentos = input(
                "\nQual a sua dúvida sobre Pedidos e Pagamentos?\n "
                "[1] Qual o prazo de aprovação do pedido?\n"
                "[2] Quais são as formas de pagamentos disponíveis?\n"
                "[3] Como faço para conseguir a 2° via do boleto?\n\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_pedidos_pagamentos == "1": #PRAZO DE APROVAÇÃO DO PEDIDO
                print("\nIsso vai depender da sua forma de pagamento. Se for cartão de crédito ou pix a compra será aprovada na mesma hora, já se for via boleto bancário a aprovação será aprovada entre 1 e 2 dia úteis")
                menu_voltar_sair()
            elif opcao_pedidos_pagamentos == "2": #FORMAS DE PAGAMENTO
                print("\nVocê pode pagar suas compras nos cartões de débito e crédito ou via pix.")
                menu_voltar_sair()
            elif opcao_pedidos_pagamentos == "3": #2° VIA DO BOLETO
                print("\nPara regerar seu boleto na loja do SQUAD 03 é preciso acessar o site da loja e clicar no menu superior que levará aos seus pedidos.Aí você entra com seu login e a respectiva senha do cadastro para ter acesso às opções da área do cliente. Uma vez logado no sistema, vá até o menu de exibição de detalhes e escolha a opção para imprimir a 2ª via do boleto. Prontinho: já regerou sua 2° via!")
                menu_voltar_sair()
            elif opcao_pedidos_pagamentos == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_pedidos_pagamentos == "5": #VOLTAR AO MENU ANTERIOR
                break
            else:
                print("Por favor, insira uma opção válida: ")
    
    elif opcoes == "3": #ENTRA NO LOOP TROCAS E DEVOLUÇÕES
        while True:
            opcao_trocas_devolucao = input(
                "\nQual a sua dúvida sobre Trocas e Devoluções?\n "
                "[1] Recebi meu pedido incompleto ou danificado.\n"
                "[2] Como funciona a política de troca e devolução?\n"
                "[3] Me arrependi da compra. E agora?\n\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_trocas_devolucao == "1": #PEDIDO INCOMPLETO OU DANIFICADO
                print("\nVocê tem até 7 dias após o recebimento do seu pedido para abrir uma solicitação de devolução via site SQUAD 03. Para investigarmos corretamente a sua situação, costumamos solicitar algumas provas que vão nos dizer porque a sua experiência não foi positiva com a compra e como podemos melhorar. Geralmente, pedimos que você anexe à sua solicitação de reembolso imagens que justifiquem o motivo do reembolso: Fotos do item recebido:Errado: item recebido de cor/tamanho diferentesDanificado: embalagem danificada, itens quebrados ou com danos (amassados, riscos)Com defeito: é comum que seja algum eletrônico, por isso, pedimos que você nos forneça alguma captura de tela com o dispositivo plugado que mostre qual é o problemaIncompleto: imagem com todos os itens recebidos no pedido caso esteja faltando alguma peça ou componente Histórico do chat ou qualquer outra evidência que nos mostre alguma negociação prévia com o vendedor (se houver)")
                menu_voltar_sair()
            elif opcao_trocas_devolucao == "2": #POLITICA TROCA E DEVOLUÇÃO
                print("\nTROCA POR DEFEITO DE FABRICAÇÃO: Caso o produto apresente defeito de fabricação em até 30 dias corridos a partir dos dados de recebimento do produto,o cliente deverá entrar em contato com nossa central de atendimento e solicitar a troca do produto.O produto deve estar em perfeitas condições, sem sinais de uso, e com embalagem original. O valor do frete da devolução do produto e da entrega.\nDEVOLUÇÃO DE PRODUTO COM DEFEITO APÓS 30 DIAS: Caso o produto apresente defeito após 30 dias corridos a partir dos dados do destinatário do produto, o cliente deverá entrar em contato com o fabricante para acionar a garantia. A loja não responderá.\nDEVOLUÇÃO POR PRODUTO DIFERENTE DO SOLICITADO: Caso o cliente receba um produto diferente do solicitado, deverá entrar em contato com a nossa central de atendimento em até 7 dias corridos a partir dos dados de recebimento do produto. A loja será responsável pelo envio do produto correto e pelo pagamento do frete da devolução do produto incorreto.")
                menu_voltar_sair()
            elif opcao_trocas_devolucao == "3": #ARREPENDIMENTO DA COMPRA
                print("\nDEVOLUÇÃO POR ARREPENDIMENTO: Caso o cliente se arrependa da compra e queira devolver o produto, deverá entrar em contato com a nossa central de atendimento em até 7 dias corridos a partir dos dados de recebimento do produto. O produto deve estar em perfeitas condições, sem sinais de uso, e com embalagem original. O valor do produto será estornado, mas o valor do frete não será reembolsado. TROCA POR INSATISFAÇÃO: Caso o cliente fique insatisfeito com o produto, mas ele esteja em perfeitas condições, sem sinais de uso, e com a embalagem original, poderá solicitar a troca do produto em até 30 dias corridos a partir dos dados de recebimento do produto . O valor do frete da devolução do produto e da entrega do novo produto será de responsabilidade do cliente.")
                menu_voltar_sair()
            elif opcao_trocas_devolucao == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_trocas_devolucao == "5": #VOLTAR AO MENU ANTERIOR
                break
            else:
                print("Por favor, insira uma opção válida: ")
                
    elif opcoes == "4": #ENTRA LOOP PRODUTOS
        while True:
            opcao_produtos = input(
                "\nQual a sua dúvida sobre Produtos?\n "
                "[1] Estou com dúvida sobre o produto. Onde tenho mais informações?\n"
                "[2] O produto que procuro não está disponível, o que faço?\n"
                "[3] Posso retirar meus produtos em alguma loja física?\n\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_produtos == "1": #DUVIDA SOBRE PRODUTO
                print("\nVocê pode entrar em contato direto com a nossa central de atendimento pelo SAC 2.0 X 3.0 X 4.0")
                menu_voltar_sair()
            elif opcao_produtos == "2": #PRODUTO INDISPONÍVEL
                print("\nVocê pode adicionar o produto a sua lista de desejos e quando o item estiver disponivel você receberá um e-mail informando que o item está disponivel para venda em nosso site.")
                menu_voltar_sair()
            elif opcao_produtos == "3": #RETIRAR PRODUTO EM LOJA FISICA
                print("\nSim, nós contamos com diversas filiais espalhadas pelo Brasil. Você pode escolher a mais próxima de você para retirar seus produtos.")
                menu_voltar_sair()
            elif opcao_produtos == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_produtos == "5": #VOLTAR AO MENU ANTERIOR
                break
            else:
                print("Por favor, insira uma opção válida: ")
                
    elif opcoes == "5": #ENTRA LOOP CADASTRO
        while True:
            opcao_cadastro = input(
                "\nQual a sua dúvida sobre Cadastro?\n "
                "[1] Como fazer meu cadastro?\n"
                "[2] Esqueci minha senha, e agora?\n"
                "[3] Como alterar ou editar  dados pessoais cadastrados no site?\n\n"
                "[4] Encerrar atendimento\n"
                "[5] Voltar ao menu anterior\n"
                "\nInsira o número referente a sua dúvida: "
            )
            if opcao_cadastro == "1": #COMO CRIAR CADASTRO
                print("\n1 - Visite o site squad03.com No canto superior direito da tela, você verá um menu marcado como 'Minha Conta'. Quando você passar o mouse sobre ele um menu suspenso irá surgir. Clique no link 'Comece Aqui/Start Here' logo abaixo do botão azul 'Inscreva-se/Sign In'.\n2 - Insira suas informações pessoais. O formulário de registro vai pedir seu nome e endereço de e-mail, além de solicitar que você escolha uma senha. Note que você também pode digitar um número de telefone. Isso não é obrigatório, mas fornece uma proteção melhor para a sua conta. O SQUAD 03 não vai te ligar, então não se preocupe com isso – esse telefone é usado apenas para fins de segurança. \n3 - Crie sua conta. Depois de preencher todas as informações necessárias, clique em 'Conta/Create Account'. Você será redirecionado imediatamente para a página de boas-vindas do SQUAD 03. Parabéns! Agora você tem uma conta oficial no site SQUAD 03.")
                menu_voltar_sair()
            elif opcao_cadastro == "2": #ESQUECI MINHA SENHA
                print("\nSe você esqueceu sua senha, poderá redefini-la usando o processo de recuperação de senha do nosso site. Para redefinir sua senha: Acesse aqui squad03/ap/forgotpassword?. Quando solicitado, insira o endereço de e-mail ou o número de celular associado à sua conta do SQUAD 03 e selecione Continuar. Enviaremos um e-mail ou SMS (dependendo do método de verificação escolhido) contendo um código de uso único para autenticar sua solicitação. Informe o código que você recebeu e selecione Continuar. Crie uma nova senha. Assim que você criar uma nova senha, ela estará ativa. Sua nova senha serve para todas as contas do SQUAD 03 associadas ao mesmo endereço de e-mail.")
                menu_voltar_sair()
            elif opcao_cadastro == "3": #EDITAR DADOS CADASTRADOS NO SITE
                print("\nAlterar as configurações da conta Você pode atualizar seu nome, endereço de e-mail, senha ou outras informações da conta. Para alterar as configurações da conta: Em Sua conta, acesse Acesso e segurança. Ao lado das informações da conta que você deseja atualizar, selecione Editar. Siga as instruções na tela e selecione Salvar alterações. Depois de concluir todas as atualizações, selecione Concluído.")
                menu_voltar_sair()
            elif opcao_cadastro == "4": #ENCERRAR ATENDIMENTO
                sair(nome)
            elif opcao_cadastro == "5": #VOLTAR AO MENU ANTERIOR
                break
            else:
                print("Por favor, insira uma opção válida: ")
    
    elif opcoes == "6": #ENCERRA O PROGRAMA - MENU PRINCIPAL
        sair(nome)
    else:
        print("Por favor, insira uma opção válida: ")