import inquirer

def get_cnh():
    pass

def get_doc_veiculo():
    pass

menu_motorista = 6


while menu_motorista == 6:
    inicial = [
        inquirer.List('Documentação',
                      message="Selecionar de quem é a documentação:",
                      choices=['Veículo', 'Motorista', 'Voltar ao Menu Anterior'], #######################################
                      ),
    ]
    documentacao = inquirer.prompt(inicial)

    if documentacao['Documentação'] == "Motorista":
        menu_motorista = [
            inquirer.List('Motorista',
                          message="Selecione a documentação",
                          choices=['Inserir documento (CNH)', 'Editar Documento', 'Visualizar Documento', 'Voltar ao Menu'],
                          ),
        ]
        documentacao_motorista = inquirer.prompt(menu_motorista)
        if documentacao_motorista['Motorista'] == "Inserir documento (CNH)":
            cnh = input("Inserir documento (CNH): ")
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial
        if documentacao_motorista['Motorista'] == "Editar Documento":
            cnh = get_cnh()
            print('Esta é sua CNH Atual: ', cnh)
            cnh = input("Inserir documento (CNH): ")
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial
        if documentacao_motorista["Motorista"] == "Visualizar Documento":
            cnh = get_cnh()
            print("Esta é sua CNH Atual: ", cnh)
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial


    if documentacao['Documentação'] == "Veículo":
        menu_veiculo = [
            inquirer.List('Veículo',
                          message="Selecione a documentação",
                          choices=['Inserir Documento do Veículo', 'Editar Documento', 'Visualizar Documento',
                                   'Voltar ao Menu'],
                          ),
        ]
        documentacao_veiculo = inquirer.prompt(menu_veiculo)

        if documentacao_veiculo["Veículo"] == "Inserir Documento do Veículo":
            doc_veiculo = input("Inserir documento (Veículo): ")
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial

        if documentacao_veiculo["Veículo"] == "Editar Documento":
            doc_veiculo = get_doc_veiculo()
            print('Este é o Documento Atual do Veículo: ', doc_veiculo)
            doc_veiculo = input("Inserir documento (Veículo): ")
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial

        if documentacao_veiculo["Veículo"] == "Visualizar Documento":
            doc_veiculo = get_doc_veiculo()
            print('Este é o Documento Atual do Veículo: ', doc_veiculo)
            ## menu_inicial = inquirer.prompt(menu)    Inciar Menu Inicial

    #else:
        #voltar ao menu inicial

#else:
    #voltar ao menu inicial