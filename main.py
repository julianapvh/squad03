from funcoes import *

print('Olá seja bem vindo(a) a loja virtal SQUAD 03\n')
nome = input("Como você gostaria de ser chamado(a)? ").capitalize() 

#
while True: 
    
    opcoes = (input(f'\n{nome}, em que podemos te ajudar? \n\n[1] - Entrega \
        \n[2] - Pedidos e Pagamentos  \n[3] - Trocas e Devolução  \n[4] - Produtos \
            \n[5] - Cadastro  \n[6] - Sair \n\nInsira um número referente ao atendimento que deseja: '))

    if opcoes == '1':
        opcoes_entrega = (input(
            '\nEscolha uma opção: \n[1] - Como rastrear meu pedido?  \n[2] - Qual o prazo de entrega do meu pedido? \
                \n[3] - Como alterar meu endereço de entrega? \n[4] - Voltar ao menu anterior '))
        
        

        if opcoes_entrega == '1':
            print('''\nDentro de “Minha conta” clique em “Meus pedidos” e procure pela sua comprinha.
                \nElas estão organizadas pelo número de identificação. Para ver mais detalhes clique em VER DETALHES.
                \nO código de rastreio deve aparecer logo abaixo do resumo da sua compra.
                \nMas lembre-se que ele aparece de formas diferentes dependendo da forma de entrega que você selecionou.
                \nCom o código de rastreio em mãos, basta você localizar a sua comprinha no site dos Correios.
                ''')

        elif opcoes_entrega == '2':
            print('\nO prazo de entrega vai depender do seu estado.')

        elif opcoes_entrega == '3':
            print('''\nOs Correios não permitem que a gente altere nenhuma informação após o despacho da sua comprinha.
                  \nPor isso, vamos ter que aguardar a sua comprinha retornar para a nossa loja para um novo despacho. 
                  ''')
        else:
             opcoes_entrega == '4'
             retornar_ao_menu_anterior

        try:
            mensagem_de_erro()
        except Exception as e:
    
         print(f'Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção... {type(e)}: e')
             

    # ================================================================================================================================================================================================================================================
    if opcoes == '2':

        opcoes_pedidos_pagamentos = (input(
            'Escolha uma opção: \n[1] - Qual o prazo de aprovação do pedido?  \n[2] - Quais são as formas de pagamentos disponíveis? \
                \n[3] - Como faço pra conseguir a 2° via do boleto? \n[4] - Voltar ao menu anterior '))

        if opcoes_pedidos_pagamentos == '1':
            print('''\nIsso vai depender da sua forma de pagamento. 
                \nSe for cartão de crédito ou pix a compra será aprovada na mesma hora, 
                \njá se for via boleto bancário a aprovação será aprovada entre 1 e 2 dia úteis
                ''')

        elif opcoes_pedidos_pagamentos == '2':
            print(
                '\nVocê pode pagar suas compras nos cartões de débito e crédito ou via pix.')

        elif opcoes_pedidos_pagamentos == '3':
            print('''\nPara regerar seu boleto na loja do SQUAD 03 é preciso acessar o site da loja e clicar no menu superior que levará aos seus pedidos.
                \nAí você entra com seu login e a respectiva senha do cadastro para ter acesso às opções da área do cliente. 
                \nUma vez logado no sistema, vá até o menu de exibição de detalhes e escolha a opção para imprimir a 2ª via do boleto. 
                \nProntinho: já regerou sua 2° via!
                ''')
            
            
        else:
            opcoes_pedidos_pagamentos == '4'
            retornar_ao_menu_anterior

         
        try:
            mensagem_de_erro()
        except Exception as e:
    
                print(f'Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção... {type(e)}: e')

            # ==========================================================================================================================================================================================================

    if opcoes == '3':
        opcoes_trocas_devolucoes = (input(
            'Escolha uma opção: \n[1] - Recebi meu pedido incompleto ou danificado.  \n[2] - Como funciona a política de troca e devolução? \
                \n[3] - Me arrependi da compra. E agora? \n[4] - Voltar ao menu anterior '))

        if opcoes_trocas_devolucoes == '1':
            print('''\nVocê tem até 7 dias após o recebimento do seu pedido para abrir uma solicitação de devolução via site SQUAD 03. 
                \nPara investigarmos corretamente a sua situação, costumamos solicitar algumas provas que vão nos dizer porque a sua 
                \nexperiência não foi positiva com a compra e como podemos melhorar. 
                \nGeralmente, pedimos que você anexe à sua solicitação de reembolso imagens que justifiquem o motivo do reembolso: 
                \nFotos do item recebido:
                \nErrado: item recebido de cor/tamanho diferentesDanificado: 
                \nembalagem danificada, itens quebrados ou com danos (amassados, riscos)Com defeito: 
                \né comum que seja algum eletrônico, por isso, pedimos que você nos forneça alguma captura de tela 
                \ncom o dispositivo plugado que mostre qual é o problemaIncompleto: imagem com todos os itens recebidos no pedido -
                \ncaso esteja faltando alguma peça ou componente 
                \nHistórico do chat ou qualquer outra evidência que nos mostre alguma negociação prévia com o vendedor (se houver)
                ''')

        elif opcoes_trocas_devolucoes == '2':
            print('''\nPolítica de Trocas e Devoluções  
                    \nTroca por defeito de fabricação:
                    \nCaso o produto apresente defeito de fabricação em até 30 dias corridos a partir dos dados de recebimento do produto,
                    \no cliente deverá entrar em contato com nossa central de atendimento e solicitar a troca do produto.
                    \nO produto deve estar em perfeitas condições, sem sinais de uso, e com embalagem original. 
                    \nO valor do frete da devolução do produto e da entrega
                    \nDevolução por produto com defeito após 30 dias : 
                    \nCaso o produto apresente defeito após 30 dias corridos a partir dos dados do destinatário do produto, o cliente deverá entrar em contato 
                    \ncom o fabricante para acionar a garantia. A loja não responderá
                    \nDevolução por produto diferente do solicitado : 
                    \nCaso o cliente receba um produto diferente do solicitado, deverá entrar em contato com a nossa central de 
                    \natendimento em até 7 dias corridos a partir dos dados de recebimento do produto. A loja será responsável 
                    \npelo envio do produto correto e pelo pagamento do frete da devolução do produto incorreto.''')

        elif opcoes_trocas_devolucoes == '3':
            print('''\nDevolução por arrependimento: Caso o cliente se arrependa da compra e queira devolver o produto, deverá entrar em contato 
                \ncom a nossa central de atendimento em até 7 dias corridos a partir dos dados de recebimento do produto. 
                \nO produto deve estar em perfeitas condições, sem sinais de uso, e com embalagem original. 
                \nO valor do produto será estornado, mas o valor do frete não será reembolsado. 
                \nTroca por insatisfação: 
                \nCaso o cliente fique insatisfeito com o produto, mas 
                \nele esteja em perfeitas condições, sem sinais de uso, e com a embalagem original, poderá solicitar a troca do produto 
                \nem até 30 dias corridos a partir dos dados de recebimento do produto . 
                \nO valor do frete da devolução do produto e da entrega do novo produto será de responsabilidade do cliente.
                ''')
        else:
            opcoes_trocas_devolucoes == '4'
            retornar_ao_menu_anterior


        try:
            mensagem_de_erro()
        except Exception as e:
    
                print(f'Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção... {type(e)}: e')

    # ========================================================================================================================================================================================================

    if opcoes == '4':
        opcoes_produtos = (input('Escolha uma opção: \n[1] - Estou com dúvida sobre o produto. Onde tenho mais informações? \
            \n[2] - O produto que procuro não está disponível, o que faço?  \n[3] - Posso retirar meus produtos em alguma loja física? \n[4] - Voltar ao menu anterior '))

        if opcoes_produtos == '1':
            print(
                '\nVocê pode entrar em contato direto com a nossa central de atendimento pelo SAC 2.0 X 3.0 X 4.0')

        elif opcoes_produtos == '2':
            print('\nVocê pode adicionar o produto a sua lista de desejos e quando o item estiver disponivel você receberá um e-mail informando que o item está disponivel para venda em nosso site.')

        elif opcoes_produtos == '3':
            print('\nSim, nós contamos com diversas filiais espalhadas pelo Brasil. Você pode escolher a mais próxima de você para retirar seus produtos.')
            
        else:
            opcoes_produtos == '4'
            retornar_ao_menu_anterior


        try:
            mensagem_de_erro()
        except Exception as e:
    
                print(f'Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção... {type(e)}: e')
    # ========================================================================================================================================================================================================================================================================

    if opcoes == '5':
        opcoes_cadastro = (input(
            'Escolha uma opção: \n[1] - Como fazer meu cadastro?  \n[2] - Esqueci minha senha, e agora? \
                \n[3] - Como alterar ou editar  dados pessoais cadastrados no site? \n[4] - Voltar ao menu anterior '))

        if opcoes_cadastro == '1':
            print('''\n1 - Visite o site squad03.com No canto superior direito da tela, você verá um menu marcado como “Minha Conta.” 
                Quando você passar o mouse sobre ele, um menu suspenso irá surgir. Clique no link "Comece Aqui/Start Here"
                logo abaixo do botão azul "Inscreva-se/Sign In". 
                \n2 - Insira suas informações pessoais. O formulário de registro vai pedir seu nome e endereço de e-mail, 
                além de solicitar que você escolha uma senha.Note que você também pode digitar um número de telefone. 
                Isso não é obrigatório, mas fornece uma proteção melhor para a sua conta. O SQUAD 03 não vai te ligar, 
                então não se preocupe com isso – esse telefone é usado apenas para fins de segurança. 
                \n3 - Crie sua conta. Depois de preencher todas as informações necessárias, clique em :
                “Criar Conta/Create Account.” Você será redirecionado imediatamente para a página de boas-vindas do SQUAD 03. 
                Parabéns! Agora você tem uma conta oficial no site SQUAD 03.
                ''')

        elif opcoes_cadastro == '2':
            print('''\nRedefinir sua senha 
                \nSe você esqueceu sua senha, poderá redefini-la usando o processo de recuperação de senha do nosso site.
                \nPara redefinir sua senha: 
                \nAcesse aqui squad03/ap/forgotpassword?. 
                \nQuando solicitado, insira o endereço de e-mail ou o número de celular associado à sua conta do SQUAD 03 e selecione Continuar.
                \nEnviaremos um e-mail ou SMS (dependendo do método de verificação escolhido) contendo um código de uso único para autenticar sua solicitação.
                \nInforme o código que você recebeu e selecione Continuar. 
                \nCrie uma nova senha. 
                \nAssim que você criar uma nova senha, ela estará ativa. Sua nova senha serve para todas as contas do SQUAD 03 associadas ao mesmo endereço de e-mail.
                ''')

        elif opcoes_cadastro == '3':
            print('''\nAlterar as configurações da conta 
                    \nVocê pode atualizar seu nome, endereço de e-mail, senha ou outras informações da conta. 
                    \nPara alterar as configurações da conta: 
                    \nEm Sua conta, acesse Acesso e segurança. 
                    \nAo lado das informações da conta que você deseja atualizar, selecione Editar. 
                    \nSiga as instruções na tela e selecione Salvar alterações. 
                    \nDepois de concluir todas as atualizações, selecione Concluído.
                ''')
            
        else:
            opcoes_cadastro == '4'
            retornar_ao_menu_anterior



        try:
            mensagem_de_erro()
        except Exception as e:
    
                print(f'Você digitou algo diferente das opções disponíveis, favor digite um número referente a uma opção... {type(e)}: e')
    # ========================================================================================================================================================================================================================================================================

    if opcoes == '6':
        sair = print(f'Obrigado por usar nosso atendimento {nome}, volte sempre!')
        break

  


 
  
 
  



