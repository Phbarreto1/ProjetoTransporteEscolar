print('===========ÁREA DOS RESPONSÁVEIS===========')

numaluno = 0
BD_alunos = {}

def solicitar_data_nasc():
    nasc_aluno = input("Digite a data de nascimento do aluno passageiro (00/00/0000): ")
    if len(nasc_aluno) == 10 and nasc_aluno[2] == '/' and nasc_aluno[5] == '/' and nasc_aluno[:2].isdigit() and nasc_aluno[3:5].isdigit() and nasc_aluno[6:].isdigit():
        return nasc_aluno
    else:
        print("Data inválida. Por favor, use o formato 00/00/0000.")
        return solicitar_data_nasc()

resposta = input("Deseja realizar alguma ação? Sim ou Não: ")

if resposta == "Sim":
    print("==MENU DE OPÇÕES==")
    print("1. Marcar ausência")
    print("2. Acessar GPS")
    print("3. Histórico de Rotas")
    print("4. Notificação e Comunicação")
    print("5. Controle de Pagamento")
    print("6. Notificações")
    print("7. Cadastro de Passageiros")
    print("8. Ajuda")
    print("9. Sair")
    opcao = int(input("Digite o número da opção escolhida: "))
    if opcao == 7:
        resposta7 = int(input("Gostaria de cadastrar um passageiro (1), editar um existente (2) ou voltar ao Menu de Opções? 1, 2 ou 3?: "))
        while resposta7 == 1:
            nome_aluno = input("Digite o nome completo do aluno passageiro:")
            cpf_aluno = input("Digite o CPF do aluno passageiro:")
            fone_aluno = input("Digite um contato telefônico do aluno passageiro:")
            endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro:")
            escola = input("Digite o nome da escola do aluno passageiro:")
            endereco_escola = input("Digite o endereço completo da escola:")
            numaluno = numaluno + 1
            BD_alunos[numaluno] = nome_aluno,cpf_aluno,solicitar_data_nasc(),fone_aluno,endereco_residencia_aluno,escola,endereco_escola
            print(f"Aluno {nome_aluno} cadastrado com sucesso!O código do aluno é {numaluno}. Salve este código para posterior consulta")
            resposta7 = int(input("Gostaria de adicionar (1) mais um passageiro, editar um existente (2) ou voltar ao Menu de Opções(3)? 1, 2 ou 3?: "))
            print(BD_alunos)
        while resposta7 == 2:
            cod_aluno = int(input("Informe o código do aluno: "))
            if cod_aluno in BD_alunos.keys():
                nome_aluno = input("Digite o nome completo do aluno passageiro:")
                cpf_aluno = input("Digite o CPF do aluno passageiro:")
                fone_aluno = input("Digite um contato telefônico do aluno passageiro:")
                endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro:")
                escola = input("Digite o nome da escola do aluno passageiro:")
                endereco_escola = input("Digite o endereço completo da escola:")
                BD_alunos[cod_aluno] = nome_aluno,cpf_aluno,solicitar_data_nasc(),fone_aluno,endereco_residencia_aluno,escola,endereco_escola
            else:
                print("Código inválido. Verifique o código correto!")
                resposta7 = int(input("Gostaria de adicionar (1) mais um passageiro, editar um existente (2) ou voltar ao Menu de Opções(3)? 1, 2 ou 3?: "))
                print(BD_alunos)
        while resposta7 == 3:

print(BD_alunos)

