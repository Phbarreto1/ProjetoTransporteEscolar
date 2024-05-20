import os
from datetime import date

os.system("clear")

cadastro = input('Já é cadastrado? [S/N]\n').upper()

if cadastro == 'N':
    while True:
        #Usar o método try-except pra tratar um eventual erro de entrada de dados.
        try:
            usuario = int(input('Cadastro:\nDigite 1 para Motorista\nDigite 2 para Responsável\n'))
            if usuario not in [1, 2]:
                print('Digite uma opção válida: 1 para Motorista ou 2 para Responsável.')
                continue
        except ValueError:
            print('Digite um número válido: 1 para Motorista e 2 para Responsável.')
            continue

        if usuario == 1:
            nome_motorista = input('Digite seu nome completo:\n')
            nascimento_motorista_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
            try:
                #Usando o método de "fromisoformat()" para converter a string do nascimento em uma variável da classe "date"
                nascimento_motorista = date.fromisoformat(nascimento_motorista_str)
            except ValueError:
                print('Data de nascimento inválida. Digite a data no formato AAAA-MM-DD.')
                continue

            cpf_motorista = input('Digite o seu CPF:\n')
            email_motorista = input('Digite o seu email:\n')
            telefone_motorista = input('Digite o seu telefone:\n')
            placa_veiculo = input('Insira a placa do veículo (sem "-"):\n')
            modelo_veiculo = input('Qual o modelo do veículo?\n')
            capacidade_veiculo = int(input('Qual é a capacidade do veículo?\n'))
            renavam_veiculo = input('Digite o RENAVAM do seu veículo:\n')
            numero_registro_cnh = input('Digite o Nº do registro da sua carteira de habilitação:\n')
            break

        elif usuario == 2:
            nome_responsavel = input('Digite seu nome completo:\n')
            nascimento_responsavel_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
            try:
                nascimento_responsavel = date.fromisoformat(nascimento_responsavel_str)
            except:
                print('Data de nascimento inválida. Digite a data no formato AAAA-MM-DD')
                continue

            cpf_responsavel = input('Digite o seu CPF:\n')
            email_responsavel = input('Digite o seu email:\n')
            telefone_responsavel = input('Digite o seu telefone:\n')
            break
elif cadastro == 'S':
    #Ajustar para centralizar as linhas
    print('---------------------------------------')
    print('                 Login                 ')
    print('---------------------------------------')
    cpf_motorista_login = input('Digite o seu CPF: ')
    cpf_motorista_senha = input('Digite a senha:')
    print('---------------------------------------')
else:
    print('Digite uma resposta válida.')