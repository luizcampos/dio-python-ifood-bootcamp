frutas = ["maçã", "banana", "pêra", "uva", "melancia", "melão"]

print(frutas[::])
print(frutas[::-1])
print(frutas[0:4])
print(frutas[0:3:2])

###### Percorrendo lista  ######

for fruta in frutas:
    print(fruta)


####### Duplicar lista ######

frutas2 = []

for fruta in frutas:
    frutas2.append(fruta)


###### MÉTODOS ######

frutas3 = frutas.copy()

print(frutas.count("maçã"))
print(frutas.extend(["maracujá", "tomate"]))
for fruta in frutas:
    print(fruta)

print("\nRetirando último elemento:\n")

frutas.pop()
for fruta in frutas:
    print(fruta)

print("\nRetirando 'melancia':\n")
frutas.remove("melancia")
for fruta in frutas:
    print(fruta)


print("\nInvertendo lista:\n")
frutas.reverse()
for fruta in frutas:
    print(fruta)

print("\nOrdenando por tamanho de caracteres:\n")
frutas.sort(key=lambda x: len(x))
for fruta in frutas:
    print(fruta)

print("\nOrdenando alfabeticamente:\n")
frutas.sort()
for fruta in frutas:
    print(fruta)

print("\nOrdenando por tamanho de caracteres com função sorted():\n")
print(sorted(frutas, key=lambda x: len(x)))



###### MATRIZ ######

matriz = [
    [0,1,2],
    [3,4,5],
    [6,7,8]
]

print("\nMatriz:\n")
print(matriz[0][2])
print(matriz[2])
