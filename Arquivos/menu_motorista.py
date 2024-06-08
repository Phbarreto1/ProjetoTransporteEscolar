import inquirer


def get_rota_manha():
    pass
def get_rota_tarde():
    pass
def get_rota_noite():
    pass


questions_menu_motorista = [
            inquirer.List('Menu Motorista',
                        message="Escolha a opção:",
                        choices=['Lista de Passageiros', 'Acessar Rotas', 'Comunicação', 'Histórico de Rotas', 'Controle de Pagamentos', 'Documentação', 'Ajuda', 'Sair'],
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
