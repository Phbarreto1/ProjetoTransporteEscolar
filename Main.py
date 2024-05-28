import os
import inquirer
import json
from datetime import date

os.system("clear")

usuarios_sistema = 'usuarios.json'

def carregar_usuarios():
    if os.path.exists(usuarios_sistema):
        with open(usuarios_sistema, 'r') as file:
            return json.load(file)
    return {}


def salvar_usuarios(usuarios):
    with open(usuarios_sistema, 'w') as file:
        json.dump(usuarios, file)


def menu_motorista():
    questions_menu_motorista = [
            inquirer.List('Menu Motorista',
                        message = "Escolha a opção:",
                        choices = ['Lista de Passageiros', 'Acessar Rotas', 'Comunicação', 'Histórico de Rotas', 'Controle de Pagamentos', 'Documentação', 'Ajuda', 'Sair'],
                        ),
    ]
    menu_motorista = inquirer.prompt(questions_menu_motorista)
    
    if menu_motorista['Menu Motorista'] == 'Lista de Passageiros':
        print("Opção escolhida: Lista de Passageiros")

    elif menu_motorista['Menu Motorista'] == 'Acessar Rotas':
        questions = [
            inquirer.List('Rota',
                    message="Qual rota você quer acessar?",
                    choices=['Manhã', 'Tarde', 'Noite','Voltar ao Menu Anterior'],
                    ),
        ]
        rota = inquirer.prompt(questions)
        if rota['Rota'] == 'Manhã':
            rota_gps = get_rota_manha()
            print('Visualizar GPS: ', rota_gps)
        if rota['Rota'] == 'Tarde':
            rota_gps = get_rota_tarde()
            print('Visualizar GPS: ', rota_gps)
        if rota['Rota'] == 'Noite':
            rota_gps = get_rota_noite()
            print('Visualizar GPS: ', rota_gps)

    elif menu_motorista['Menu Motorista'] == 'Comunicação':
        print("Opção escolhida: Comunicação")

    elif menu_motorista['Menu Motorista'] == 'Histórico de Rotas':
        print("Opção escolhida: Histórico de Rotas")

    elif menu_motorista['Menu Motorista'] == 'Controle de Pagamentos':
        print("Opção escolhida: Controle de Pagamentos")

    elif menu_motorista['Menu Motorista'] == 'Documentação':
        print("Opção escolhida: Documentação")

    elif menu_motorista['Menu Motorista'] == 'Ajuda':
        print("Opção escolhida: Ajuda")

    elif menu_motorista['Menu Motorista'] == 'Sair':
        print("Saindo...")  


def menu_responsavel():
    questions_menu_responsavel = [
            inquirer.List('Menu Responsável',
                        message="Escolha a opção:",
                        choices=['Marcar Ausência', 'Acessar GPS', 'Histórico de Rotas', 'Notificações e Comunicação','Controle de Pagamentos', 'Documentação', 'Cadastro de Passageiros', 'Ajuda', 'Sair'],
                        ),
    ]       
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
        placa_veiculo = input('Insira a placa do veículo (sem "-"):\n')
        modelo_veiculo = input('Qual o modelo do veículo?\n')
        capacidade_veiculo = int(input('Qual é a capacidade do veículo?\n'))
        renavam_veiculo = input('Digite o RENAVAM do seu veículo:\n')
        numero_registro_cnh = input('Digite o Nº do registro da sua carteira de habilitação:\n')
        senha_motorista = input('Crie uma senha:\n')

        codigo_motorista = str(contador_usuarios).zfill(4)
        contador_usuarios += 1

        usuarios[cpf_motorista] = {
            'nome': nome_motorista,
            'nascimento': nascimento_motorista_str,
            'email': email_motorista,
            'telefone': telefone_motorista,
            'placa_veiculo': placa_veiculo,
            'modelo_veiculo': modelo_veiculo,
            'capacidade_veiculo': capacidade_veiculo,
            'renavam_veiculo': renavam_veiculo,
            'numero_registro_cnh': numero_registro_cnh,
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
            'tipo': 'responsavel'
            }

        salvar_usuarios(usuarios)

        print(f'Responsável cadastrado! Código do usuário: {codigo_responsavel}')
        login()
else:

    login()