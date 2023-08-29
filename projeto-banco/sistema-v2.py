
saldo, deposito, saque, saques_dia  = 0, 0, 0, 0
LIMITE_SAQUES = 3
extrato = ""
usuarios = {
    1: {"nome":"Luiz Fellipe", "dataNascimento": "29/09/1999", "cpf": "25874136988", "endereco": "João Santos, 287 - Pelourinho - Lorena/SP"}
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
    qtde = len(usuarios)

    nome = str(input("Digite o nome: "))
    data = str(input("Digite a data de nascimento (ex: 10/05/2001): "))
    cpf = str(input("Digite o CPF: "))

    if int(cpf) > 0:
        print("cpf válido")
    else:
        print("cpf inválido")

    #verificar se cpf existe

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

    print(usuarios)
    

#def criar_conta_corrente():


def listar_usuarios():
    global usuarios

    for chave, valor in usuarios.items():
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

    elif opcao == "6":
        listar_usuarios()
        
    elif opcao == "0":
        print("Sistema encerrado. Obrigado!")
        break

    else:
        print("Opção inválida!")
        continue

