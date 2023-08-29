
saldo, deposito, saque, saques_dia  = 0, 0, 0, 0
LIMITE_SAQUES = 3
extrato = ""
menu = f"""
======================
=        MENU        =
======================
=   1 - Depositar    =
=   2 - Sacar        = 
=   3 - Ver Extrato  =
=   0 - Sair         = 
======================
Digite um número: """  

while True:
    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Valor a depositar: R$"))
        if deposito < 0:
            print("Por favor, digite um valor válido!")
        else:
            saldo += deposito
            extrato += f"""\nDepósito: +R${deposito:.2f}\nSaldo =    R${saldo:.2f}"""
            print(f"Seu depósito de R${deposito} foi realizado com sucesso.")

    elif opcao == "2":

        if saques_dia < LIMITE_SAQUES:
            saque = float(input("Valor a sacar: R$"))
            if saque < 0:
                print("Por favor, digite um valor válido!\n")
            elif saque > saldo:
                print("Saldo insuficiente. Confira seu extrato no menu anterior!\n")
            elif saque > 500.0:
                print("Limite do saque atual: R$500.\nDigite um novo valor!\n")
            else:
                saldo -= saque
                extrato += f"""\nSaque: -R${saque:.2f}\nSaldo = R${saldo:.2f}"""
                saques_dia+=1
                print(f"Seu saque de R${saque} foi realizado com sucesso.\nVocê pode sacar mais {LIMITE_SAQUES-saques_dia} hoje ainda.")
        else:
            print(f"Limite de saque diário excedido.")

    elif opcao == "3":
        print("\n======================\n=  EXTRATO COMPLETO  =\n======================")
        print("  Sem movimentações." if not extrato else extrato)

    elif opcao == "0":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Opção inválida!")
        continue