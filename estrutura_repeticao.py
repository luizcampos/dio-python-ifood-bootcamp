
frase = input("Digite algo: ")
VOGAIS = "AEIOU"

# FOR 
for letra in frase:
    if letra.upper() in VOGAIS:
        print(letra, end="-")

print() #pula linha



# FOR / ELSE
for letra in frase:
    if letra.upper() in VOGAIS:
        print(letra, end="-")
else:
    print("\nExecuta ao final do laço")


# FOR + RANGE

for num in range(0,10):
    print(num, end=(" - "))

print() 

for num in range(0,51,5):  #tabuada do 5.  Conta de 0 a 50, pulando de 5 em 5.
    print(num, end=(" - "))



# WHILE (quando não sabemos quantas vezes rodar)

while num != 22:
    num = int(input("\nAdivinhe o número: "))

    if num != 0:
        print("Continue tentando!")

else:
    print(f"Você acertou! O número era {num}")


print() 


# BREAK E CONTINUE

for n in range(100):

    if n == 50:
        break  # para tudo e sai do laço

    if n % 2 == 0:
        continue   #pula o restante e volta pro laço

    print(n, end=(" - "))
