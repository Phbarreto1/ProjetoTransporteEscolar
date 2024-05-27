import os
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


contador_usuarios = 1

usuarios = carregar_usuarios()

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
            break

        elif usuario == 2:
            nome_responsavel = input('Digite seu nome completo:\n')
            nascimento_responsavel_str = input('Digite sua data de nascimento (AAAA-MM-DD):\n')
            try:
                nascimento_responsavel = date.fromisoformat(nascimento_responsavel_str)
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
            break
elif cadastro == 'S':

    def login():
        cpf_login = input('Digite o seu CPF (apenas os números): ')
        senha_login = input('Digite a sua senha: ')

        usuarios = carregar_usuarios()
        if cpf_login in usuarios and usuarios[cpf_login]['senha'] == senha_login:
            print('Login com sucesso!')
            print(f'Bem-vindo(a), {usuarios[cpf_login]['nome']}!')
        else:
            print('CPF ou senha incorretos. Tente novamente.')

    login()
    
  
else:
    print('Digite uma resposta válida.')