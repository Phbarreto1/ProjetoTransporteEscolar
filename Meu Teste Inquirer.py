import inquirer


def get_rota_manha():
    pass
def get_rota_tarde():
    pass
def get_rota_noite():
    pass

menu_motorista = 2

if menu_motorista == 2:
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
