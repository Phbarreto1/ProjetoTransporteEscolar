import inquirer



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
