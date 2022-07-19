# Guardar NOME do cliente - ok
# Guardar MESA do cliente - ok
# Apresentar CARDÁPIO de comida - ok
# Apresentar CARDÁPIO de bebida - ok
# Guardar pedido
# Fechar a conta mostrando valor total
import os

fechar_conta = False

cardapio_pizza = {
    "Pizza de Calabresa":15.50,
    "Pizza de Bacon":15.00,
    "Pizza de Quatro Queijos":15.70
}
opcao_comida = False

cardapio_bebidas = {
    "Coca-Cola Lata":7.50,
    "Suco de Laranja Copo": 9.00,
    "Cerveja Lata": 5.50
}
opcao_bebida = False

pedido_cliente = {}

menu_op = True

vlr_pedido_comida = 0

vlr_pedido_bebida = 0

nome_cliente = input("Diga seu nome: ")
numero_mesa = input("Em qual mesa você está? ")

def titulo(txt):
    print("\033[36m-\033[0;0m" *40)
    print("\033[36m"+txt+"\033[0;0m")
    print("\033[36m-\033[0;0m" *40)

def num_opcao(msg):
    while True:
        try:
            op = int(input(msg))
        except(ValueError, TypeError):
            print("\033[31mDigite uma opção válida.\33[m")
        except(KeyboardInterrupt):
            print("\033[31mUsuário preferiu não digitar esse número.\33[m")
        else:
            return op

def resposta():
    while True:
        resp = input("Deseja constinuar? [S/N]").upper()[0]
        if resp in 'SN':
            break
        print("ERRO! Digite apenas S / N")
    if resp == "N":
        print("Saindo")

def vlr_conta():
    fechar_conta = True
    if fechar_conta == True:
        soma_total = vlr_pedido_bebida + vlr_pedido_comida
        print("Valor da conta: ",soma_total)
        print("\033[36m-\033[0;0m" *40)

def pedido_pizza():
    os.system("cls")
    titulo("ESCOLHA DE PIZZA".center(40))
    print("1-Pizza de Calabresa\n2-Pizza de Bacon\n3-Pizza de Quatro Queijos\n4-Voltar")
    print("\033[36m-\033[0;0m" *40)

    opcao = num_opcao("Digite a opção de sua escolha: ")
    if opcao == 1:
        print("Você adicionou uma Pizza de Calabresa. Deseja algo mais?")
        vlr_pedido_comida += cardapio_pizza["Pizza de Calabresa"]
    elif opcao == 2:
        print("Você adicionou uma Pizza de Bacon. Deseja algo mais?")
        vlr_pedido_comida += cardapio_pizza["Pizza de Bacon"]
    elif opcao == 3:
        print("Você adicionou uma Pizza de Quatro Queijos. Deseja algo mais?")
        vlr_pedido_comida += cardapio_pizza["Pizza de Quatro Queijos"]
    elif opcao == 4:
        menu()
    else:
        print("\033[31mOpção inválida. Digite uma opção válida!\33[m")

def pedido_bebida():
    os.system("cls")
    titulo("ESCOLHA DE BEBIDAS".center(40))
    print("1-Coca-Cola Lata\n2-Suco de Laranja Copo\n3-Cerveja Lata\n4-Voltar")
    print("\033[36m-\033[0;0m" *40)

    opcao = num_opcao("Digite a opção de sua escolha: ")
    if opcao == 1:
        print("Você adicionou uma Coca-Cola Lata. Deseja algo mais?")
        vlr_pedido_bebida += cardapio_bebidas["Coca-Cola Lata"]
    elif opcao == 2:
        print("Você adicionou um Copo de Suco de Laranja. Deseja algo mais?")
        vlr_pedido_bebida += cardapio_bebidas["Suco de Laranja Copo"]
    elif opcao == 3:
        print("Você adicionou uma Cerveja Lata. Deseja algo mais?")
        vlr_pedido_bebida += cardapio_bebidas["Cerveja Lata"]
    elif opcao == 4:
        menu()
    else:
        print("\033[31mOpção inválida. Digite uma opção válida!\33[m")

def menu():
    os.system("cls")
    print ("Olá",nome_cliente, "\nvocê está na mesa número", numero_mesa)
    print("\033[36m-\033[0;0m" *40)
    print("")
    while menu_op == True:
            print("Opção 1 - Abrir Cardápio de Pizza\nOpção 2 - Abrir Cardápio de Bebidas\nOpção 3 - Fazer pedido\nOpção 4 - Fechar conta\nOpção 5 - Encerrar")
            print("")
            opcao = num_opcao("Qual opcão deseja? ")
            if opcao == 1:
                opcao_comida = True
                if opcao_comida == True:
                    for chave in cardapio_pizza.keys():
                        print(f'{chave} : Valor {cardapio_pizza[chave]}\n')
                        print("")
            elif opcao == 2:
                opcao_bebida = True
                if opcao_bebida == True:
                    for chave in cardapio_bebidas.keys():
                        print(f'{chave} : Valor {cardapio_bebidas[chave]}')
                        print("")
            elif opcao == 3:
                pedido_pizza()
                resposta()
                pedido_bebida()
                resposta()
            elif opcao == 4:
                vlr_conta()
            elif opcao == 5:
                print("-----Encerrando-----")
                break
            else:
                print("Digite uma opção válida!")
    os.system("pause")
menu()