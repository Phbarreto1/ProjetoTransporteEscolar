import inquirer

numaluno = 0
BD_alunos = {}

def solicitar_data_nasc():
    nasc_aluno = input("Digite a data de nascimento do aluno passageiro (00/00/0000): ")
    if len(nasc_aluno) == 10 and nasc_aluno[2] == '/' and nasc_aluno[5] == '/' and nasc_aluno[:2].isdigit() and nasc_aluno[3:5].isdigit() and nasc_aluno[6:].isdigit():
        return nasc_aluno
    else:
        print("Data inválida. Por favor, use o formato 00/00/0000.")
        return solicitar_data_nasc()

def menu_responsavel():
    questions_menu_responsavel = [inquirer.List('Menu Responsável',message="Escolha a opção:",choices=['Marcar Ausência', 'Acessar GPS', 'Histórico de Rotas', 'Notificações e Comunicação','Controle de Pagamentos', 'Documentação', 'Cadastro de Passageiros', 'Ajuda', 'Sair'],),]
    menu_responsavel = inquirer.prompt(questions_menu_responsavel)

    if menu_responsavel['Menu Responsável'] == 'Marcar Ausência':
        print("Opção escolhida: Marcar Ausência")

    elif menu_responsavel['Menu Responsável'] == 'Acessar GPS':
        print("Opção escolhida: Marcar Ausência")

    elif menu_responsavel['Menu Responsável'] == 'Histórico de Rotas':
        print("Opção escolhida: Histórico de Rotas")

    elif menu_responsavel['Menu Responsável'] == 'Notificações e Comunicação':
        print("Opção escolhida: Notificações e Comunicação")

    elif menu_responsavel['Menu Responsável'] == 'Controle de Pagamentos':
        print("Opção escolhida: Controle de Pagamentos")

    elif menu_responsavel['Menu Responsável'] == 'Documentação':
        print("Opção escolhida: Documentação")

    elif menu_responsavel['Menu Responsável'] == 'Cadastro de Passageiros':
        print("Opção escolhida: Cadastro de Passageiros")

    elif menu_responsavel['Menu Responsável'] == 'Ajuda':
        print("Opção escolhida: Ajuda")

    elif menu_responsavel['Menu Responsável'] == 'Sair':
        print("Saindo...")

def submenu_cadastro_passageiros():
    questions_submenu_cadastro_passageiros = [inquirer.List('SubMenu Cadastro Passageiros',message="Escolha a opção:",choices=['Novo cadastro', 'Editar cadastro', 'Voltar ao menu principal'],),]
    resposta_submenu_cadastro_passageiros = inquirer.prompt(questions_submenu_cadastro_passageiros)

    if resposta_submenu_cadastro_passageiros['SubMenu Cadastro Passageiros'] == 'Novo cadastro':
        cadastrar_passageiro(BD_alunos, numaluno)

    elif resposta_submenu_cadastro_passageiros['SubMenu Cadastro Passageiros'] == 'Editar cadastro':
        editar_passageiro(BD_alunos)

    elif resposta_submenu_cadastro_passageiros['SubMenu Cadastro Passageiros'] == 'Voltar ao menu principal':
        menu_responsavel()

def cadastrar_passageiro(BD_alunos, numaluno):
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


def editar_passageiro(BD_alunos):
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

def Iniciar():
    print('===========ÁREA DOS RESPONSÁVEIS===========')
    menu_responsavel()
    submenu_cadastro_passageiros()

Iniciar()

