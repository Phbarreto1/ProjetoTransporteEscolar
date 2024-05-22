import inquirer

def get_filhos():
    return ['Maria', 'João']

menu_responsavel = 1

while menu_responsavel == 1:
    ausencia = [
        inquirer.List('Ausências',
                      message="Selecionar qual horário não será necessário",
                      choices=['Manhã', 'Tarde', 'Noite', 'Voltar ao Menu Anterior'], #######################################
                      ),
    ]
    turno_ausencia = inquirer.prompt(ausencia)


    filhos = get_filhos()
    qtd_filhos = len(filhos)

    if qtd_filhos >1:
        filho = [
            inquirer.List('Filho',
                          message="Selecionar qual o filho",
                          choices=filhos #######################################
                          ),
        ]

        filho_ausencia = inquirer.prompt(filho)

    print("Filho para ausencia: ", filho_ausencia['Filho'])
    print("Turno: ", turno_ausencia["Ausências"])
