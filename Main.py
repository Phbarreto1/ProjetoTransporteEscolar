import os
from datetime import date

os.system("clear")

cadastro = input('Já é cadastrado? [S/N]\n').upper()

if cadastro == 'N':
    usuario = input('Cadastro:\nDigite 1 para Motorista\nDigite 2 para Responsável\n').lower()
    while True:
        if usuario == 1:
            nome_motorista = input('Digite seu nome completo:\n')
            nascimento_motorista_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
            #Usando o método de "fromisoformat()" para converter a string do nascimento em uma variável da classe "date" 
            nascimento_motorista = date.fromisoformat(nascimento_motorista_str) 
            cpf_motorista = input('Digite o seu CPF:\n')
            email_motorista = input('Digite o seu email:\n')
            telefone_motorista = input('Digite o seu telefone:\n')
            placa_veiculo = input('Insira a placa do veículo (sem "-"):\n')
            modelo_veiculo = input('Qual o modelo do veículo?\n')
            capacidade_veiculo = int(input('Qual é a capacidade do veículo?\n'))
            renavam_veiculo = input('Digite o RENAVAM do seu veículo:\n')
            numero_registro_cnh = input('Digite o Nº do registro da sua carteira de habilitação:\n')
            #Criar número de registro do motorista
            break
            

        elif usuario == 2:
            nome_responsavel = input('Digite seu nome completo:\n')
            nascimento_responsavel_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
            nascimento_responsavel = date.fromisoformat(nascimento_responsavel_str)
            cpf_responsavel = input('Digite o seu CPF:\n')
            email_responsavel = input('Digite o seu email:\n')
            telefone_responsavel = input('Digite o seu telefone:\n')
            #Criar número de registro do responsável
            break
elif cadastro == 'S':
    print('--------------------------------------')
    print('Login')
    print('--------------------------------------')
    cpf_motorista_login = input('Digite o seu CPF: ')
    cpf_motorista_senha = input('Digite a senha:')
    print('--------------------------------------')