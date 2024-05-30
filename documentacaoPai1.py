'''
#Abrir laço WHILE para selecionar a documentação.
                    Se documento = 1:
                         - Abre documentos do motorista:
                              Se documento_motorista = 1:
                                   - Inserir documento (CNH);
                           Senão se documento_motorista = 2:
                                - Editar documento;
                           Senão se documento_motorista = 3:
                                - Visualizar documento;
                           Senão se documento_motorista = 4:
                                - Voltar ao menu de documentação (2.1.6);
                           Senão:
                                - Opção inválida.
                 Senão se documento = 2:
                      - Abre documentos do veículo:
                              Se documento_veiculo = 1:
                                   - Inserir documento (do veículo);
                           Senão se documento_veiculo = 2:
                                - Editar documento;
                           Senão se documento_veiculo = 3:
                                - Visualizar documento;
                           Senão se documento_veiculo = 4:
                                - Voltar ao menu de documentação (2.1.6);
                           Senão:
                                - Opção inválida.
                 Senão se documento = 3:
                      - Voltar ao menu do Motorista (2.1)
'''
while True:
    # Exibir opções para o responsável
    print("\n1: Visualizar documento do motorista")
    print("2: Visualiza documento do carro")
    print("3: Sair")

    documentacao = input("\nEscolha a documentação: ")
    
    if documentacao == "1":
        print("Documentação do motarista")
    elif documentacao == "2":
        print("Documentação do carro")
    elif documentacao == "3":
        print("Voltar para o menu")
        break
    else:
        print("Opção inválida")