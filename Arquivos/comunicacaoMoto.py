'''
2.1.3 Comunicação (3ª Opção):
		Se selecionar mais de um passageiro:
		#Abrir laço WHILE para selecionar as mensagens automáticas.
		     Abrir menu de mensagens automáticas
		          Se mensagem = 1:
		               - O passageiro/aluno foi entregue à escola;
		          Senão se mensagem = 2:
		               - O passageiro/aluno foi apanhado na escola e está voltando para casa;
		          Senão se mensagem = 3:
		               - Houve um problema com o transporte;
		          Senão se mensagem = 4:
			   - Personalizar mensagem;
		          Senão se mensagem = 5:
			   - Voltar ao menu do Motorista (2.1);
		          Senão:
			   - Opção inválida.
		Se selecionar um passageiro:
		     Abrir conversa privada com o responsável.
		     #Aqui temos a opção de colocar mensagens automáticas ou não.
'''
mensagem = 0
while True:
	mensagem = int(input("Mensagens automáticas: "))
	if mensagem == 1:
		print("Chegando em 10 minutos")
	elif mensagem == 2:
		print("Chegando em 5 minutos")
	elif mensagem == 3:
		print("Esperando o aluno")
	elif mensagem == 4:
		print("O aluno foi entregue a escola")
	elif mensagem == 5:
		print("O aluno está voltando para casa")
	elif mensagem == 6:
		print("Houve um problema com o transporte")
	elif mensagem == 7:
		mensagem_personalizada = input("Digite a mensagem que deseja enviar: ")
		print(mensagem_personalizada)
	elif mensagem == 8:
		print("Voltar ao menu")
		break
	else:
		print("Opção inválida")