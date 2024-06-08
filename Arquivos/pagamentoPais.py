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
    print("\n1: Sim \n2: Não \n3: Suporte \n4: Menu")
    pagamento = int(input("\nJá fez seu pagamento? "))
    if pagamento == 1:
        print("Sim")
    elif pagamento == 2:
        print("Não")
        gerar_boleto = int(input("Deseja gerar o boleto? (1: Sim)"))
        if gerar_boleto == 1:
            print("Gerando boleto")
        else:
            break
    elif pagamento == 3:
        print("Suporte")
    elif pagamento == 4:
        print("Voltando para o menu")
        break
    else:
        print("Opção inválida")