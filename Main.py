import os
import inquirer
import json
from datetime import date

os.system("clear")

usuarios_sistema = 'usuarios.json'
lista_mensagens_enviadas = [] # armazenar as notificações enviadas pelo motorista
passageiros = []
num_aluno = 0
BD_alunos = {}

def carregar_usuarios():
    if os.path.exists(usuarios_sistema):
        with open(usuarios_sistema, 'r') as file:
            return json.load(file)
    return {}


def salvar_usuarios(usuarios):
    with open(usuarios_sistema, 'w') as file:
        json.dump(usuarios, file)
    

def cadastrar_passageiro(BD_alunos, num_aluno):
    nome_aluno = input("Digite o nome completo do aluno passageiro:\n")
    data_nasc_aluno = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
    while True:
        try:
            nascimento_aluno = date.fromisoformat(data_nasc_aluno)
            break
        except ValueError:
            print('Data de nascimento inválida. Digite a data no formato AAAA-MM-DD.')
            continue
    cpf_aluno = input("Digite o CPF do aluno passageiro:\n")
    fone_aluno = input("Digite um contato telefônico do aluno passageiro:\n")
    endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro:\n")
    escola = input("Digite o nome da escola do aluno passageiro:\n")
    endereco_escola = input("Digite o endereço completo da escola:\n")
    turno = [
        inquirer.List('Turno',
                    message = "Selecione o turno do passageiro:",
                    choices = ['Manhã', 'Tarde', 'Noite']  
                    ),
    ]
    turno_escolhido = inquirer.prompt(turno)['Turno']

    num_aluno = len(passageiros) + 1
    passageiro = {'nome': nome_aluno, 'nascimento': data_nasc_aluno, 'codigo': num_aluno, 'turno': turno_escolhido}
    passageiros.append(passageiro)
    BD_alunos[num_aluno] = (nome_aluno, nascimento_aluno, cpf_aluno, fone_aluno, endereco_residencia_aluno, escola, endereco_escola)
    print(f"Aluno {nome_aluno} cadastrado com sucesso! O código do aluno é {num_aluno}. Salve este código para posterior consulta")
    return num_aluno


def visualizar_passageiros(turno=None):
    if turno:
        passageiros_filtrados = [p for p in passageiros if p['turno'] == turno]
        if not passageiros_filtrados:
            print(f'Nenhum passageiro cadastrado para o turno {turno}.\n')
            return
    else:
        passageiros_filtrados = passageiros
        if not passageiros_filtrados:
            print('Nenhum passageiro cadastrado.\n')
            return

    while True:
        print('Lista de Passageiros:')
        for passageiro in passageiros_filtrados:
            print(f"Código: {passageiro['codigo']} - Nome: {passageiro['nome']}")

        selecionar_passageiro = [
            inquirer.List('Passageiro',
                        message = "Selecione um passageiro para incluir na rota:",
                        choices = [f"{p['codigo']} - {p['nome']}" for p in passageiros_filtrados] + ['Voltar ao Menu'],
                        ),
        ]
        resposta_passageiro = inquirer.prompt(selecionar_passageiro)

        if resposta_passageiro['Passageiro'] == 'Voltar ao Menu':
            break

        codigo_selecionado = int(resposta_passageiro['Passageiro'].split(' ')[0])
        passageiro_selecionado = next(p for p in passageiros_filtrados if p['codigo'] == codigo_selecionado)
        print(f"Passageiro {passageiro_selecionado['nome']} selecionado para a rota.\n")


def editar_passageiro(BD_alunos):
    cod_aluno = int(input("Informe o código do aluno: "))
    if cod_aluno in BD_alunos:
        nome_aluno = input("Digite o nome completo do aluno passageiro: ")
        cpf_aluno = input("Digite o CPF do aluno passageiro: ")
        fone_aluno = input("Digite um contato telefônico do aluno passageiro: ")
        endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro: ")
        escola = input("Digite o nome da escola do aluno passageiro: ")
        endereco_escola = input("Digite o endereço completo da escola: ")
        BD_alunos[cod_aluno] = (nome_aluno, cpf_aluno, fone_aluno, endereco_residencia_aluno, escola, endereco_escola)
        print(f"Aluno {nome_aluno} com código {cod_aluno} editado com sucesso!")
    else:
        print("Código inválido. Verifique o código correto!")


def voltar_ao_menu():
    pergunta_voltar_menu = [
            inquirer.List('Voltar',
                        message = "Voltar ao menu?",
                        choices = ['Sim', 'Não'],  
                        ),       
    ]
    resposta_voltar_menu = inquirer.prompt(pergunta_voltar_menu)
    return resposta_voltar_menu['Voltar'] == 'Sim'


def menu_motorista():
    cnh = None
    doc_veiculo = None

    while True:
        questions_menu_motorista = [
                inquirer.List('Menu Motorista',
                            message = "Escolha a opção",
                            choices = ['Lista de Passageiros', 'Acessar Rotas', 'Comunicação', 'Histórico de Rotas', 'Controle de Pagamentos', 'Documentação', 'Ajuda', 'Sair'],
                            ),
        ]
        menu_motorista = inquirer.prompt(questions_menu_motorista)
        
        if menu_motorista['Menu Motorista'] == 'Lista de Passageiros':
            visualizar_passageiros()
            voltar_ao_menu()    

        elif menu_motorista['Menu Motorista'] == 'Acessar Rotas':
            pergunta_acesso_rota = [
                inquirer.List('Rota',
                            message = "Qual rota você quer acessar?",
                            choices =['Manhã', 'Tarde', 'Noite', 'Voltar ao Menu Anterior'],
                            ),
            ]
            rota = inquirer.prompt(pergunta_acesso_rota)

            if rota['Rota'] == 'Manhã':
                visualizar_passageiros('Manhã')
                voltar_ao_menu()
            if rota['Rota'] == 'Tarde':
                visualizar_passageiros('Tarde')
                voltar_ao_menu()
            if rota['Rota'] == 'Noite':
                visualizar_passageiros('Noite')
                voltar_ao_menu()
                        
        elif menu_motorista['Menu Motorista'] == 'Comunicação':
            while True:
                mensagens_motorista = [
                        inquirer.List('Mensagens Motorista',
                                    message = "Escolha a opção:",
                                    choices = ['Chegando em 10 minutos', 'Chegando em 5 minutos', 'Estou aqui', 'O aluno foi entregue à escola', 'O aluno está voltando para casa',
                                               'Houve um problema com o transporte', 'Personalizar mensagem', '']    
                                    ),                   
                ]
                mensagem = inquirer.prompt(mensagens_motorista)

                if mensagem['Mensagens Motorista'] == 'Chegando em 10 minutos':
                    print('Chegando em 10 minutos\n')
                    mensagem_enviada = 'Chegando em 10 minutos'
                elif mensagem['Mensagens Motorista'] == 'Chegando em 5 minutos':
                    print('Chegando em 5 minutos\n')
                    mensagem_enviada = 'Chegando em 5 minutos'
                elif mensagem['Mensagens Motorista'] == 'Estou aqui':
                    print('Estou aqui\n')
                    mensagem_enviada = 'Estou aqui'
                elif mensagem['Mensagens Motorista'] == 'O aluno foi entregue à escola':
                    print('O aluno foi entregue à escola\n')
                    mensagem_enviada = 'O aluno foi entregue à escola'
                elif mensagem['Mensagens Motorista'] == 'O aluno está voltando para casa':
                    print('O aluno está voltando para casa\n')
                    mensagem_enviada = 'O aluno está voltando para casa'
                elif mensagem['Mensagens Motorista'] == 'Houve um problema com o transporte':
                    print('Houve um problema com o transporte\n')
                    mensagem_enviada = 'Houve um problema com o transporte'
                elif mensagem['Mensagens Motorista'] == 'Personalizar mensagem':
                    mensagem_enviada = input('Escreva a mensagem que deseja enviar:\n')
            
                lista_mensagens_enviadas.append(mensagem_enviada)
                print('Mensagem Enviada!\n')

                if voltar_ao_menu():
                    break

        elif menu_motorista['Menu Motorista'] == 'Histórico de Rotas':
            while True:
                    historico = input('Gostaria de visualizar uma rota realizada? [S/N]\n').upper()
                    if historico == 'S':
                        historico_de_rotas_str = input('Escolha a data da rota que deseja visualizar (AAAA-MM-DD):\n')
                        historico_rota = date.fromisoformat(historico_de_rotas_str)
                        print(f'\nVisualizando a rota do GPS no dia: {historico_rota}...\n')
                        historico = input('Gostaria de visualizar outra rota? [S/N]\n').upper()
                        if historico == 'S':
                            historico_de_rotas_str = input('Escolha a data da rota que deseja visualizar (AAAA-MM-DD):\n')
                            historico_rota = date.fromisoformat(historico_de_rotas_str)
                            print(f'\nVisualizando a rota do GPS no dia: {historico_rota}...\n')
                        else:
                            voltar_ao_menu()
                    else:
                        break
            voltar_ao_menu()
            
        elif menu_motorista['Menu Motorista'] == 'Controle de Pagamentos':
            while True:
                pergunta_pagamentos_motorista = [
                inquirer.List('Pagamentos',
                            message = "Escolha a opção",
                            choices = ['Editar chave PIX', 'Suporte', 'Voltar ao menu'],
                            ),
                ]
                pagamento_motorista = inquirer.prompt(pergunta_pagamentos_motorista)
                
                if pagamento_motorista['Pagamentos'] == 'Editar chave PIX':
                    chave_pix = input('Digite a nova chave do PIX:\n')
                    voltar_ao_menu()
                elif pagamento_motorista['Pagamento'] == 'Suporte':   
                    suporte__pagamentos_motorista = input('Envie para nós o seu problema:\n')
                    print('\nMensagem enviada com sucesso! Em breve o nosso suporte entrará em contato.\n')
                    voltar_ao_menu()
                else:
                    voltar_ao_menu()
                        
        elif menu_motorista['Menu Motorista'] == 'Documentação':
            perguntas_documentacao_motorista = [
                inquirer.List('Escolher Documentações',
                            message = "Selecionar qual o tipo de documentação:",
                            choices = ['Motorista', 'Veículo', 'Voltar ao menu'],
                            ),
            ]
            documentacao = inquirer.prompt(perguntas_documentacao_motorista)

            if documentacao['Escolher Documentações'] == 'Motorista':
                while True:
                    menu_motorista = [
                        inquirer.List('Motorista',
                                    message = "Selecione a documentação",
                                    choices = ['Editar documento', 'Visualizar documento', 'Voltar ao menu'],
                                    ),
                    ]
                    documentacao_motorista = inquirer.prompt(menu_motorista)

                    if documentacao_motorista['Motorista'] == 'Editar Documento':
                        numero_registro_cnh = input('Editar documento (CNH): ')
                        voltar_ao_menu()
                    elif documentacao_motorista['Motorista'] == 'Visualizar Documento':
                        if numero_registro_cnh:
                            print(f'Esta é sua CNH Atual: {numero_registro_cnh}')
                        else:
                            print('Nenhum documento encontrado.')
                        voltar_ao_menu()
                    elif documentacao_motorista['Motorista']  == 'Voltar ao menu':
                        break
                    voltar_ao_menu()                       
               
            elif documentacao['Escolher Documentações'] == 'Veículo':
                while True:
                    menu_veiculo = [
                        inquirer.List('Veículo',
                                    message = "Selecione a documentação",
                                    choices = ['Editar documento', 'Visualizar documento', 'Voltar ao menu'],
                                    ),
                    ]
                    documentacao_veiculo = inquirer.prompt(menu_veiculo)
                                     
                    if documentacao_veiculo['Veículo'] == 'Editar Documento':
                        doc_veiculo = input('Inserir novo documento (Veículo): ')
                        voltar_ao_menu()                   
                    elif documentacao_veiculo['Veículo'] == 'Visualizar Documento':
                        if doc_veiculo:
                            print(f'Este é o Documento Atual do Veículo: {doc_veiculo}')
                        else:
                            print('Nenhum documento encontrado.')
                        voltar_ao_menu()
                    elif documentacao_veiculo['Veículo'] == 'Voltar ao menu':
                        break
            
            elif documentacao['Escolher Documentações'] == 'Voltar ao menu':
                voltar_ao_menu()

        elif menu_motorista['Menu Motorista'] == 'Ajuda':
            perguntas_menu_ajuda_motorista = [
                    inquirer.List('Menu Ajuda',
                                message = "Escolha a opção:",
                                choices = ['Sobre o menu', 'Denúncia', 'Falar com o suporte', 'Voltar ao menu'],  
                                ),
            ]
            resposta_ajuda_motorista = inquirer.prompt(perguntas_menu_ajuda_motorista)

            if resposta_ajuda_motorista['Menu Ajuda'] == 'Sobre o menu':
                print(
                "Bem-vindo ao Menu de Ajuda! Aqui você encontrará uma explicação detalhada de cada opção disponível no Menu do Motorista:\n"
                "1. Lista de Passageiros: Nessa opção você irá definir as rotas selecionando os passageiros específicos de cada turno;\n"
                "2. Acessar Rotas: Opção do menu para acessar as rotas definidas anteriormente. Ao selecionar uma rota salva, o GPS mostrará o percurso a ser realizado;\n"
                "3. Histórico de Rotas: Aqui você pode acessar o histórico completo das rotas percorridas pelo transporte escolar. Isso inclui datas, horários e o trajeto realizado, proporcionando maior transparência e segurança;\n"
                "4. Controle de Pagamentos: Edite sua chave PIX ou entre em contato com o suporte financeiro;\n"
                "5. Documentação: Edite ou visualize o seu documento ou o do seu veículo;\n"
                "6. Ajuda: Esta opção leva você ao menu de ajuda, onde você pode encontrar informações detalhadas sobre o uso de todas as funcionalidades do aplicativo, além de dicas e suporte para resolver eventuais problemas;\n"
                "7. Sair: Use esta opção para sair da sua conta de forma segura. Certifique-se de que todas as suas informações estão salvas antes de sair.\n")
                voltar_ao_menu() 

            elif resposta_ajuda_motorista['Menu Ajuda'] == 'Denúncia':
                denuncia_motorista = input('Gostaria de fazer uma denúncia? Explique-nos abaixo o problema ocorrido:\n')
                print('Denúncia enviada! Aguarde um momento, logo entraremos em contato...')
                voltar_ao_menu()

            elif resposta_ajuda_motorista['Menu Ajuda'] == 'Falar com o suporte':
                suporte_motorista = input('Informe-nos o problema e o nosso suporte entrará em contato!')
                print('Mensagem enviada!')
                voltar_ao_menu()

            else:
                voltar_ao_menu()

        elif menu_motorista['Menu Motorista'] == 'Sair':
            print("Saindo...")
            break


def menu_responsavel():
    while True:
        perguntas_menu_responsavel = [
                inquirer.List('Menu Responsável',
                            message = "Escolha a opção:",
                            choices = ['Marcar Ausência', 'Acessar GPS', 'Histórico de Rotas', 'Notificações e Comunicação','Controle de Pagamentos', 'Documentação', 'Cadastro de Passageiros', 'Ajuda', 'Sair'],
                            ),
        ]       
        menu_responsavel = inquirer.prompt(perguntas_menu_responsavel)

        if menu_responsavel['Menu Responsável'] == 'Marcar Ausência':
            
            def receber_filhos():
                return['Maria', 'João']
            
            menu_responsavel = 1

            while menu_responsavel == 1:
                ausencia = [
                        inquirer.List('Ausências',
                                    message = "Selecionar qual horário não será necessário",
                                    choices = ['Manhã', 'Tarde', 'Noite', 'Voltar ao Menu Anterior'],
                                    ),
                ]
                turno_ausencia = inquirer.prompt(ausencia)

                filhos = receber_filhos()
                qtd_filhos = len(filhos)

                if qtd_filhos > 1:
                    filho = [
                            inquirer.List('Filho',
                                        message = "Selecionar qual o filho",
                                        choice = filhos 
                                        ),
                    ]
                    filho_ausencia = inquirer.prompt(filho)

                    print("Filho para ausencia: ", filho_ausencia['Filho'])
                    print("Turno: ", turno_ausencia["Ausências"])

            voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Acessar GPS':
            pergunta_acesso_gps = [
                    inquirer.List('Perguntas Acesso GPS',
                                message = "Deseja visualizar a localização em tempo real?",  
                                choices = ['Sim', 'Não'],
                                )
            ]
            resposta_acesso_gps = inquirer.promp(pergunta_acesso_gps)

            if resposta_acesso_gps ['Perguntas Acesso GPS'] == 'Sim':
                print('>>> Visualizando localização em tempo real do veículo <<<')
                voltar_ao_menu()
            else:
                voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Histórico de Rotas':
            while True:
                historico = input('Gostaria de visualizar uma rota realizada anteriormente? [S/N]\n').upper()
                if historico == 'S':
                    historico_de_rotas_str = input('Escolha a data da rota que deseja visualizar (AAAA-MM-DD):\n')
                    try:
                        historico_rota = date.fromisoformat(historico_de_rotas_str)
                        print(f'Visualizando a rota do GPS no dia: {historico_rota}')
                        if historico == 'S':
                            historico_de_rotas_str = input('Escolha a data da rota que deseja visualizar (AAAA-MM-DD):\n')
                            historico_rota = date.fromisoformat(historico_de_rotas_str)
                            print(f'\nVisualizando a rota do GPS no dia: {historico_rota}...\n')
                        else:
                            voltar_ao_menu()
                    except ValueError:
                        print('Data inválida. Digite no formato AAAA-MM-DD')                
                else:
                    voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Notificações e Comunicação':
            print("Visualizando chat com o motorista...")
            notificacoes = ['Notificação 1', 'Notificação 2', 'Notificação 3']
            for notificacao in notificacoes:
                print(notificacao)

            enviar_mensagem = [
                inquirer.List('Enviar Mensagem',
                            message = "Deseja enviar uma mensagem?",  
                            choices = ['Sim', 'Não'] 
                            ),
            ]
            resposta_chat = inquirer.prompt(enviar_mensagem)

            if resposta_chat['Enviar Mensagem'] == 'Sim':
                mensagem_personalizada = input('Escreva a mensagem que deseja enviar: ')
                print(f'Mensagem enviada: "{mensagem_personalizada}"')
                voltar_ao_menu()

            else:
                voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Controle de Pagamentos':
            while True:
                pagamento_responsavel = [
                        inquirer.List('Pagamentos Menu Responsável',
                                    message = "Escolha a opção",
                                    choices = ['Baixar boleto', 'Alterar data de vencimento', 'Suporte', 'Voltar ao menu']
                                    ),
                ]
                resposta_pagamento = inquirer.prompt(pagamento_responsavel)

                if resposta_pagamento['Pagamentos Menu Responsável'] == 'Baixar Boleto':
                    print('Baixando boleto...')
                    print('boleto_mensalidade.pdf')
                    voltar_ao_menu()
                elif resposta_pagamento['Pagamentos Menu Responsável'] == 'Alterar data de vencimento':
                    data_vencimento = int(input('Gostaria de alterar o vencimento para o dia 05, 10, 15, 20 ou 25?\n'))
                    print(f'Vencimento alterado para o dia {data_vencimento}!')
                    voltar_ao_menu()
                elif resposta_pagamento['Pagamentos Menu Responsável'] == 'Suporte':
                    suporte_pagamentos_responsavel = input('Envie para nós o seu problema que iremos entrar em contato para resolvê-lo.\n')
                    voltar_ao_menu()
                else:
                    voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Documentação':
            perguntas_documentacao_responsavel = [
                inquirer.List('Escolher Documentações',
                            message = "Selecionar qual o tipo de documentação:",
                            choices = ['Motorista', 'Veículo', 'Voltar ao menu'],
                            ),
            ]
            documentacao_responsavel = inquirer.prompt(perguntas_documentacao_responsavel)

            if documentacao_responsavel['Escolher Documentações'] == 'Motorista':
                print(f'CNH do motorista {numero_registro_cnh}')
                voltar_ao_menu()                
            elif documentacao_responsavel['Escolher Documentações'] == 'Veículo':
                print(f'O documento do veículo {renavam_veiculo}')
                voltar_ao_menu()
            else:
                voltar_ao_menu()
                
        elif menu_responsavel['Menu Responsável'] == 'Cadastro de Passageiros':
            pergunta_cadastrar_passageiros = [
                    inquirer.List('SubMenu Cadastro de Passageiros',
                                message = "Escolha a opção:",  
                                choices = ['Novo cadastro', 'Editar cadastro', 'Voltar ao menu']  
                                ),
            ]
            resposta_cadastrar_passageiros = inquirer.prompt(pergunta_cadastrar_passageiros)

            if resposta_cadastrar_passageiros['Submenu Cadastro de Passageiros'] == 'Novo cadastro':
                cadastrar_passageiro(BD_alunos, num_aluno)
                voltar_ao_menu()
            elif resposta_cadastrar_passageiros['SubMenu Cadastro de Passageiros'] == 'Editar cadastro':
                editar_passageiro(BD_alunos)
                voltar_ao_menu()
            else:
                voltar_ao_menu()
            
        elif menu_responsavel['Menu Responsável'] == 'Ajuda':
            perguntas_menu_ajuda_responsavel = [
                    inquirer.List('Menu Ajuda',
                                message = "Escolha a opção:",
                                choices = ['Sobre o menu', 'Denúncia', 'Falar com o suporte', 'Voltar ao menu'],  
                                ),
            ]
            resposta_ajuda_responsavel = inquirer.prompt(perguntas_menu_ajuda_responsavel)

            if resposta_ajuda_responsavel['Menu Ajuda'] == 'Sobre o menu':
                print(
                "Bem-vindo ao Menu de Ajuda! Aqui você encontrará uma explicação detalhada de cada opção disponível no Menu do Responsável:\n"
                "1. Marcar Ausência: Use esta opção para informar ao serviço de transporte que seu filho estará ausente em um determinado dia. Isso ajuda a evitar esperas desnecessárias e a planejar melhor a rota.\n"
                "2. Acessar GPS: Esta funcionalidade permite que você visualize a localização em tempo real do transporte escolar. Assim, você pode acompanhar o trajeto e saber exatamente onde está o veículo.\n"
                "3. Histórico de Rotas: Aqui você pode acessar o histórico completo das rotas percorridas pelo transporte escolar. Isso inclui datas, horários e o trajeto realizado, proporcionando maior transparência e segurança.\n"
                "4. Notificações e Comunicação: Nesta seção, você encontrará todas as notificações importantes enviadas pelo serviço de transporte. Também é possível enviar e receber mensagens diretamente, facilitando a comunicação entre responsáveis e prestadores de serviço.\n"
                "5. Controle de Pagamentos: Mantenha seu controle financeiro em dia com esta funcionalidade. Verifique datas de vencimento e detalhes de transações, além de acessar os pagamentos pendentes.\n"
                "6. Documentação: Aqui você pode acessar e enviar documentos importantes relacionados ao serviço de transporte, como autorização de viagem, atestados médicos e outras documentações necessárias para garantir a segurança e o bem-estar dos passageiros.\n"
                "7. Cadastro de Passageiros: Mantenha os dados dos passageiros sempre atualizados. Nesta seção, você pode adicionar, editar ou remover informações sobre os passageiros, garantindo que todos os detalhes estejam corretos e atualizados.\n"
                "8. Ajuda: Esta opção leva você ao menu de ajuda, onde você pode encontrar informações detalhadas sobre o uso de todas as funcionalidades do aplicativo, além de dicas e suporte para resolver eventuais problemas.\n"
                "9. Sair: Use esta opção para sair da sua conta de forma segura. Certifique-se de que todas as suas informações estão salvas antes de sair.\n")
                voltar_ao_menu()

            elif resposta_ajuda_responsavel['Menu Ajuda'] == 'Denúncia':
                denuncia_responsavel = input('Gostaria de fazer uma denúncia? Explique-nos abaixo o problema ocorrido:\n')
                print('Denúncia enviada! Aguarde um momento, logo entraremos em contato...')
                voltar_ao_menu()

            elif resposta_ajuda_responsavel['Menu Ajuda'] == 'Falar com o suporte':
                suporte_responsavel = input('Informe-nos o problema e o nosso suporte entrará em contato!')
                print('Mensagem enviada!')
                voltar_ao_menu()

            else:
                voltar_ao_menu()

        elif menu_responsavel['Menu Responsável'] == 'Sair':
            print("Saindo...")
            break


def login():
    cpf_login = input('\nDigite o seu CPF (apenas os números): ')
    senha_login = input('\nDigite a sua senha: ')


    usuarios = carregar_usuarios()
    if cpf_login in usuarios and usuarios[cpf_login]['senha'] == senha_login:
        print('Login com sucesso!')
        print(f'Bem-vindo(a), {usuarios[cpf_login]['nome']}!')
        if usuarios[cpf_login]['tipo'] == 'motorista':
                menu_motorista()
        elif usuarios[cpf_login]['tipo'] == 'responsavel':
                menu_responsavel()
    else:
        print('CPF ou senha incorretos. Tente novamente.')
        login()


contador_usuarios = 1
usuarios = carregar_usuarios()

    
login_usuario = [
    inquirer.List('Tela Inicial',
                message = "Já é cadastrado?",
                choices = ['Não, seguir para o Cadastro', 'Sim, seguir para o Login']                    
                ),
]
    
resposta_login = inquirer.prompt(login_usuario)

if resposta_login['Tela Inicial'] == 'Não, seguir para o Cadastro':    
    cadastrar_usuario_novo = [
        inquirer.List('Cadastrar',
                    message = "Escolha uma das opções para se cadastrar",
                    choices =['Motorista', 'Passageiro'] 
                    ),        
    ]
    cadastrar = inquirer.prompt(cadastrar_usuario_novo)
    
    if cadastrar['Cadastrar'] == 'Motorista':
        nome_motorista = input('Digite seu nome completo:\n')
        nascimento_motorista_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
        while True:
            try:
                #Usando o método de "fromisoformat()" para converter a string do nascimento em uma variável da classe "date"
                nascimento_motorista = date.fromisoformat(nascimento_motorista_str)
                break
            except ValueError:
                print('Data de nascimento inválida. Digite a data no formato AAAA-MM-DD.')
                continue

        cpf_motorista = input('Digite o seu CPF (apenas os números):\n')
        email_motorista = input('Digite o seu email:\n')
        telefone_motorista = input('Digite o seu telefone:\n')
        endereco_motorista = input('Digite o seu endereço:\n')
        placa_veiculo = input('Insira a placa do veículo (sem "-"):\n')
        modelo_veiculo = input('Qual o modelo do veículo?\n')
        capacidade_veiculo = int(input('Qual é a capacidade do veículo?\n'))
        renavam_veiculo = input('Digite o RENAVAM do seu veículo:\n')
        numero_registro_cnh = input('Digite o Nº do registro da sua carteira de habilitação:\n')
        chave_pix = input('Digite a sua chave PIX:\n')
        senha_motorista = input('Crie uma senha:\n')

        codigo_motorista = str(contador_usuarios).zfill(4)
        contador_usuarios += 1

        usuarios[cpf_motorista] = {
            'nome': nome_motorista,
            'nascimento': nascimento_motorista_str,
            'email': email_motorista,
            'telefone': telefone_motorista,
            'endereco_motorista': endereco_motorista,
            'placa_veiculo': placa_veiculo,
            'modelo_veiculo': modelo_veiculo,
            'capacidade_veiculo': capacidade_veiculo,
            'renavam_veiculo': renavam_veiculo,
            'numero_registro_cnh': numero_registro_cnh,
            'chave_pix': chave_pix,
            'senha': senha_motorista,
            'codigo': codigo_motorista,
            'tipo': 'motorista'
            }
            
        salvar_usuarios(usuarios)

        print(f'Motorista cadastrado! Código do usuário: {codigo_motorista}')
        login()

    else:
        nome_responsavel = input('Digite seu nome completo:\n')
        nascimento_responsavel_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
        while True:
            try:
                nascimento_responsavel = date.fromisoformat(nascimento_responsavel_str)
                break
            except:
                print('Data de nascimento inválida. Digite a data no formato AAAA-MM-DD')
                continue

        cpf_responsavel = input('Digite o seu CPF (apenas os números):\n')
        endereco_responsavel = input('Digite o seu endereço:\n')
        email_responsavel = input('Digite o seu email:\n')
        telefone_responsavel = input('Digite o seu telefone:\n')
        senha_responsavel = input('Crie uma senha: ')

        codigo_responsavel = str(contador_usuarios).zfill(4)
        contador_usuarios += 1

        usuarios[cpf_responsavel] = {
            'nome': nome_responsavel,
            'nascimento': nascimento_responsavel_str,
            'email': email_responsavel,
            'telefone': telefone_responsavel,
            'senha': senha_responsavel,
            'codigo': codigo_responsavel,
            'endereço': endereco_responsavel,
            'tipo': 'responsavel'
            }

        salvar_usuarios(usuarios)

        print(f'Responsável cadastrado! Código do usuário: {codigo_responsavel}')
        login()
else:

    login()