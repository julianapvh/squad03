def saudacao(boas_vindas):
  print('Olá seja bem vindo(a)a SQUAD 03')
  
while True:
    opcoes = (input('Escolha uma opção: \n[1] - Entrega \n[2] - Pedidos e Pagamentos \n[3] - Trocas e Devolução \n[4] - Produtos \n[5] - Cadastro \n[6] - Sair \n'))
    if opcoes == '1':
        opcoes_entrega = (input('Escolha uma opção: \n[1] - Como rastrear meu pedido? \n[2] - Qual o prazo de entrega do meu pedido? \n[3] - Como alterar meu endereço de entrega? \n'))
    if opcoes_entrega == '1':
        print('Copie o código de rastreio, recebido em seu e-mail e cole no site dos correios.')
    elif opcoes_entrega == '2':
        print('O prazo de entrega vai depender do seu estado.')   
    elif opcoes_entrega == '3':
        print('O prazo de entrega vai depender do seu estado.')   
    elif opcoes_entrega == '3':
        print('Entre no site e altere o endereço.')
    break
else:
    print('Escolha uma opção válida!')
    


 
  
 
  




