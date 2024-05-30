'''
   2.1.5 Pagamentos (5ª Opção):
		#Abrir laço WHILE para selecionar a visualização da área de pagamentos.
                    Se pagamentos = 1:
                         - Visualizar painel/histórico de pagamentos recebidos (informações dos usuários, datas e valores);
                    Senão se pagamentos = 2:    
		          - Saque (transferência bancária ou outra opção)
		     Senão se pagamentos = 3:
                        - Suporte;
                    Senão se pagamentos = 4:
		         - Voltar ao menu do Motorista (2.1);
'''
pagamento = 0
while True:
    pagamento = int(input("Opcão de pagamento: "))
    if pagamento == 1:
        print("Histórico de pagamento \nFevereiro - Pago \nMarço - Pago \nAbril - Pago \nMaio - Pago \nJunho - Aguardando pagamento")
    elif pagamento == 2:
        print("Transferência bancária")
    elif pagamento == 3:
        print("Pix")
    elif pagamento == 4:
        print("Boleto")
    elif pagamento == 5:
        print("Suporte")
    elif pagamento == 6:
        break
    