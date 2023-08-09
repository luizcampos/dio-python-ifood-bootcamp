
saldo = 1000

def sacar(valor):     # método
    if saldo > valor:
        print("Saque realizado!")

sacar(200)


if 1000 > 5000:
    print("1000 é maior que 5000")
elif 1000 > 2000:
    print("1000 não é maior que 2000")
else:
    print("1000 não é maior que 5000")


#If ternário

resul = "Sucesso" if saldo > 200 else "Falha"
print(resul + " ao realizar o saque!")
print(f"{resul} ao realizar o saque!")