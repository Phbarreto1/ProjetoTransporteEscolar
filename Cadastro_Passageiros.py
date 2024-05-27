def solicitar_data_nasc():
    nasc_aluno = input("Digite a data de nascimento do aluno passageiro (00/00/0000): ")
    if len(nasc_aluno) == 10 and nasc_aluno[2] == '/' and nasc_aluno[5] == '/' and nasc_aluno[:2].isdigit() and nasc_aluno[3:5].isdigit() and nasc_aluno[6:].isdigit():
        return nasc_aluno
    else:
        print("Data inválida. Por favor, use o formato 00/00/0000.")
        return solicitar_data_nasc()


def cadastrar_aluno(BD_alunos, numaluno):
    nome_aluno = input("Digite o nome completo do aluno passageiro: ")
    cpf_aluno = input("Digite o CPF do aluno passageiro: ")
    fone_aluno = input("Digite um contato telefônico do aluno passageiro: ")
    endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro: ")
    escola = input("Digite o nome da escola do aluno passageiro: ")
    endereco_escola = input("Digite o endereço completo da escola: ")
    numaluno += 1
    BD_alunos[numaluno] = (nome_aluno, cpf_aluno, solicitar_data_nasc(), fone_aluno, endereco_residencia_aluno, escola, endereco_escola)
    print(f"Aluno {nome_aluno} cadastrado com sucesso! O código do aluno é {numaluno}. Salve este código para posterior consulta")
    return numaluno


def editar_aluno(BD_alunos):
    cod_aluno = int(input("Informe o código do aluno: "))
    if cod_aluno in BD_alunos:
        nome_aluno = input("Digite o nome completo do aluno passageiro: ")
        cpf_aluno = input("Digite o CPF do aluno passageiro: ")
        fone_aluno = input("Digite um contato telefônico do aluno passageiro: ")
        endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro: ")
        escola = input("Digite o nome da escola do aluno passageiro: ")
        endereco_escola = input("Digite o endereço completo da escola: ")
        BD_alunos[cod_aluno] = (nome_aluno, cpf_aluno, solicitar_data_nasc(), fone_aluno, endereco_residencia_aluno, escola, endereco_escola)
        print(f"Aluno {nome_aluno} com código {cod_aluno} editado com sucesso!")
    else:
        print("Código inválido. Verifique o código correto!")


def menu_de_opcoes():
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


def Iniciar():
    print('===========ÁREA DOS RESPONSÁVEIS===========')
    numaluno = 0
    BD_alunos = {}

    while True:
        resposta = input("Deseja realizar alguma ação? Sim ou Não: ")
        if resposta.lower() == "sim":
            while True:
                menu_de_opcoes()
                try:
                    opcao = int(input("Digite o número da opção escolhida: "))
                    if opcao == 7:
                        while True:
                            resposta7 = int(input("Gostaria de cadastrar um passageiro (1), editar um existente (2) ou voltar ao Menu de Opções (3)? 1, 2 ou 3?: "))
                            if resposta7 == 1:
                                numaluno = cadastrar_aluno(BD_alunos, numaluno)
                            elif resposta7 == 2:
                                editar_aluno(BD_alunos)
                            elif resposta7 == 3:
                                break
                            else:
                                print("Opção inválida. Tente novamente.")
                    elif opcao == 9:
                        print("Saindo...Programa finalizado.")
                        return  # Adicione esta linha para sair do loop e da função main
                    else:
                        print("Opção inválida. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número.")
        elif resposta.lower() == "não":
            print("Saindo...Programa finalizado.")
            break
        else:
            print("Resposta inválida. Por favor, responda com 'Sim' ou 'Não'.")

Iniciar()

