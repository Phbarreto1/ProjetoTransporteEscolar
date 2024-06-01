import inquirer

def menu_responsavel():
    questions_menu_responsavel = [inquirer.List('Menu Responsável',message="Escolha a opção:",choices=['Marcar Ausência', 'Acessar GPS', 'Histórico de Rotas', 'Notificações e Comunicação','Controle de Pagamentos', 'Documentação', 'Cadastro de Passageiros', 'Ajuda', 'Sair'],),]
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
        print(
	"AJUDA - MENU RESPONSÁVEL\n"
	"Bem-vindo ao Menu de Ajuda! Aqui você encontrará uma explicação detalhada de cada opção disponível no Menu Responsável:\n"
	"1.Marcar Ausência: Use esta opção para informar ao serviço de transporte que seu filho estará ausente em um determinado dia.Isso ajuda a evitar esperas desnecessárias e a planejar melhor a rota.\n"
	"2.Acessar GPS: Esta funcionalidade permite que você visualize a localização em tempo real do transporte escolar. Assim, você pode acompanhar o trajeto e saber exatamente onde está o veículo.\n"
	"3.Histórico de Rotas: Aqui você pode acessar o histórico completo das rotas percorridas pelo transporte escolar. Isso inclui datas, horários e o trajeto realizado, proporcionando maior transparência e segurança.\n"
	"4.Notificações e Comunicação: Nesta seção, você encontrará todas as notificações importantes enviadas pelo serviço de transporte. Também é possível enviar e receber mensagens diretamente, facilitando a comunicação entre responsáveis e prestadores de serviço.\n"
	"5.Controle de Pagamentos: Mantenha seu controle financeiro em dia com esta funcionalidade. Verifique os pagamentos realizados, datas de vencimento e detalhes de transações, além de acessar os pagamentos pendentes.\n"
	"6.Documentação: Aqui você pode acessar e enviar documentos importantes relacionados ao serviço de transporte, como autorização de viagem, atestados médicos e outras documentações necessárias para garantir a segurança e o bem-estar dos passageiros.\n"
	"7.Cadastro de Passageiros: Mantenha os dados dos passageiros sempre atualizados. Nesta seção, você pode adicionar, editar ou remover informações sobre os passageiros, garantindo que todos os detalhes estejam corretos e atualizados.\n"
	"8.Ajuda: Esta opção leva você ao menu de ajuda, onde você pode encontrar informações detalhadas sobre o uso de todas as funcionalidades do aplicativo, além de dicas e suporte para resolver eventuais problemas.\n"
    "9.Sair: Use esta opção para sair da sua conta de forma segura. Certifique-se de que todas as suas informações estão salvas antes de sair.\n")

    elif menu_responsavel['Menu Responsável'] == 'Sair':
        print("Saindo...")

def Iniciar():
    print('===========ÁREA DOS RESPONSÁVEIS===========')
    menu_responsavel()

Iniciar()

