
saldo, deposito, saque, saques_dia  = 0, 0, 0, 0
LIMITE_SAQUES = 3
extrato = ""
usuarios = {
    1: {"nome":"Luiz Fellipe", "dataNascimento": "29/09/1999", "cpf": "25874136988", "endereco": "João Santos, 287 - Pelourinho - Lorena/SP"}
}
contas = {
    1: {"agencia": "0001", "usuario": "25874136988", "conta": 1}
}
menu = f"""================================
=             MENU             =
================================
=   1 - Depositar              =
=   2 - Sacar                  = 
=   3 - Ver Extrato            =
=   4 - Cadastrar usuário      =
=   5 - Criar conta corrente   =
=   6 - Listar usuários        =
=   7 - Listar contas          =
=   8 - Excluir usuário        =
=   0 - Sair                   = 
================================
Digite um número: """  

def sacar(*, limite_diario, saldo, extrato, saques_dia):
    if saques_dia < limite_diario:
        saque = float(input("Valor a sacar: R$"))
        if saque < 0:
            print("Por favor, digite um valor válido!\n")
        elif saque > saldo:
            print("Saldo insuficiente. Confira seu extrato no menu anterior!\n")
        elif saque > 500.0:
            print("Limite do saque atual: R$500.\nDigite um novo valor!\n")
        else:
            saldo -= saque
            extrato += f"""\nSaque: -R${saque:.2f}\nSaldo = R${saldo:.2f}\n"""
            saques_dia+=1
            print(f"Seu saque de R${saque} foi realizado com sucesso.\nVocê pode sacar mais {limite_diario-saques_dia} hoje ainda.")
            return extrato, saldo, saques_dia
    else:
        print(f"Limite de saque diário excedido.")
        return extrato, saldo, saques_dia

def depositar(saldo, extrato, /):
    deposito = float(input("Valor a depositar: R$"))
    if deposito < 0:
        print("Por favor, digite um valor válido!")
        return extrato, saldo
    else:
        saldo += deposito
        extrato += f"""\nDepósito: +R${deposito:.2f}\nSaldo =    R${saldo:.2f}\n"""
        print(f"Seu depósito de R${deposito} foi realizado com sucesso.")
        return extrato, saldo

def gerar_extrato(*, extrato):
    print("\n================================\n=       EXTRATO COMPLETO       =\n================================")
    print("  Sem movimentações." if not extrato else extrato)

def criar_usuario():
    global usuarios
    sucesso, cpf_existe = False, False
    qtde = len(usuarios)

    nome = str(input("Digite o nome: "))
    data = str(input("Digite a data de nascimento (ex: 10/05/2001): "))
    
    while sucesso == False:
        aux = False
        cpf = input("Digite o CPF (apenas números): ")

        if cpf != "":
            if  len(cpf) == 11:
                #verificar se cpf existe
                for chave, valor in usuarios.items():
                    if usuarios[chave]["cpf"] == str(cpf):
                        print("CPF já existe! Tente novamente")
                        aux = True
                        break
                    else:
                        aux = False
                if aux == False:
                    try:
                        int(cpf) #só numeros?
                    except ValueError as e:
                        print("CPF inválido!")
                    else:
                        sucesso = True  #é só num, converteu pra int
                        break
            else:
                print("CPF inválido! Digite um CPF com 11 caracteres")

        else:
            print("CPF inválido!")

    rua = str(input("Digite o nome rua: "))
    num = str(input("Digite o nº da casa: "))
    bairro = str(input("Digite o bairro: "))
    cidade = str(input("Digite a cidade: "))
    sigla = str(input("Digite o estado (apenas sigla): "))
    endereco = f"{rua}, {num} - {bairro} - {cidade}/{sigla}"

    usuarios.setdefault(qtde+1, {})
    usuarios[qtde+1]["nome"] = nome
    usuarios[qtde+1]["data"] = data
    usuarios[qtde+1]["cpf"] = cpf
    usuarios[qtde+1]["endereco"] = endereco
    

def criar_conta_corrente():
    global contas, usuarios
    qtde = len(contas)
    sucesso = False

    contas.setdefault(qtde+1, {})
    contas[qtde+1]["agencia"] = "0001"

    while sucesso == False:
        user = str(input("Digite o CPF do cliente: "))

        if user != "":
            #verificar se usuário existe
            for chave, valor in usuarios.items():
                if usuarios[chave]["cpf"] == user:
                    try:
                        int(user) #só numeros?
                    except ValueError as e:
                        print("Cliente inválido!")
                    else:
                        contas[qtde+1]["usuario"] = user
                        sucesso = True  #é só num, converteu pra int
                        break

            if sucesso == False:
                print("Usuário não encontrado!")
        else:
            print("Usuário inválido!")
    
    contas[qtde+1]["conta"] = int(contas[qtde]["conta"])+1

    #sucesso = False
    #contaExist = True

    # while sucesso == False:
    #     conta = str(input("Digite o número da conta: "))

    #     if conta != "":
    #         #verificar se conta existe
    #         for chave, valor in usuarios.items():
    #             print(chave, contas[chave]["conta"], conta)
    #             if contas[chave]["conta"] == conta:
    #                     print("Conta já existe! Tente novamente")
    #                     break
    #             else:
    #                 contaExist = False
            
    #         if contaExist == False:
    #             try:
    #                 int(conta) #só numeros?
    #             except ValueError as e:
    #                 print("Número da conta inválida!")
    #             else:
    #                 contas[qtde+1]["conta"] = conta
    #                 sucesso = True  #é só num, converteu pra int
    #                 break
    #     else:
    #         print("Número da conta inválida!")

def excluir_cliente():

    global usuarios
    sucesso = False

    while sucesso == False:
        cpf = str(input("Digite o CPF do usuário: "))
        if cpf != "":
                #verificar se usuário existe
                for chave, valor in usuarios.items():
                    if usuarios[chave]["cpf"] == cpf:
                        try:
                            int(cpf) #só numeros?
                        except ValueError as e:
                            print("Usuário inválido!")
                        else:
                            del usuarios[chave]
                            sucesso = True
                            print("Usuário excluído com sucesso!")
                            break
        else:
            print("CPF inválido! Tente novamente")

def listar_usuarios():
    global usuarios

    print("Sem usuários cadastrados" if not usuarios else "")

    for chave, valor in usuarios.items():
        print(chave, valor)

def listar_contas():
    global contas

    for chave, valor in contas.items():
        print(chave, valor)

while True:
    opcao = input(menu)

    if opcao == "1":
        infosAtuaisDep = list(depositar(saldo, extrato))
        #print(infosAtuaisDep)
        extrato = str(infosAtuaisDep[0])
        saldo = float(infosAtuaisDep[1])

    elif opcao == "2":
        infosAtuaisSaq = list(sacar(limite_diario=LIMITE_SAQUES, saldo=saldo, extrato=extrato, saques_dia=saques_dia))
        extrato = str(infosAtuaisSaq[0])
        saldo = float(infosAtuaisSaq[1])
        saques_dia = int(infosAtuaisSaq[2])

    elif opcao == "3":
        gerar_extrato(extrato=extrato)

    elif opcao == "4":
        criar_usuario()
    
    elif opcao == "5":
        criar_conta_corrente()

    elif opcao == "6":
        listar_usuarios()

    elif opcao == "7":
        listar_contas()

    elif opcao == "8":
        excluir_cliente()
        
    elif opcao == "0":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Opção inválida!")
        continue

