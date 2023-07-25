
num1 = 10
num2 = 3

## Aritméticos

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 ** num2)
print(num1 % num2)

print(num1 + num2 / 2)
print((num1 + num2) / 2)

## Comparação

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)
print(num1 != num2)

## Atribuição

num1 = 500
num2 += 100
num1 *= 5
num1 **= 2
num2 //=2

print(num1, num2)

## Lógico

print(True and True)
print(True and False)
print(True or False)

print((num1 > 10) and (num2 > 0)) 

print(not num1 > 10) ## negação

## Identidade a

nome = "Luiz"
nome2 = nome
num3, num4 = 10, 10

print(nome is nome2)
print(nome is not nome2)
print(num3 is num4)
print(num1 is num2)


##Associação

frase = "I'm one of one"
frutas = ["limão", "uva"]

print("Associação\n","one" in frase)
print("one" not in frase)
print("maçã" in frutas)
print("Limão" in frutas) ##sensitivo
