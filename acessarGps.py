''' Acassar GPS '''

acessar_gps = 0
while True:
    acessar_gps = int(input("Acesso ao GPS: "))
    if acessar_gps == 1:
        print("Localização em tempo real")
    elif acessar_gps == 2:
        break
    else:
        print("Opção inválida")