print('=======CADASTRO DOS ALUNOS PASSAGEIROS======')

def solicitar_data():
    nasc_aluno = input("Digite a data de nascimento do aluno passageiro (00/00/0000): ")
    if len(nasc_aluno) == 10 and nasc_aluno[2] == '/' and nasc_aluno[5] == '/' and nasc_aluno[:2].isdigit() and nasc_aluno[3:5].isdigit() and nasc_aluno[6:].isdigit():
        return nasc_aluno
    else:
        print("Data inválida. Por favor, use o formato 00/00/0000.")
        return solicitar_data()

nome_aluno = input("Digite o nome completo do aluno passageiro:")
cpf_aluno = input("Digite o CPF do aluno passageiro:")
solicitar_data()
fone_aluno = input("Digite um contato telefônico do aluno passageiro:")
endereco_residencia_aluno = input("Digite o endereço completo da residência do aluno passageiro:")
escola = input("Digite o nome da escola do aluno passageiro:")
endereco_escola = input("Digite o endereço completo da escola:")