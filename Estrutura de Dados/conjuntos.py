
# CONJUNTOS

linguagens = set(("python", "c", "java", "c+"))

print(linguagens)

numeros = {1, 2, 3, 4, 5}

for num in numeros:
    print(num)


# MÉTODOS

conjuntoA = {1, 2, 3}
conjuntoB = {3, 4, 5}

print(conjuntoA.union(conjuntoB))

print(conjuntoA.intersection(conjuntoB))

print(conjuntoA.difference(conjuntoB))

print(conjuntoA.symmetric_difference(conjuntoB))

print(conjuntoA.issubset(conjuntoB))

print(conjuntoA.issuperset(conjuntoB))

print(conjuntoA.isdisjoint(conjuntoB))

conjuntoA.add(15)
print(conjuntoA)

conjuntoC = conjuntoA.copy()
print(conjuntoC)


print(conjuntoC.pop())
print(conjuntoC)

conjuntoC.discard(15)
print(conjuntoC)

print(len(conjuntoC))

print(conjuntoC.clear())
print(conjuntoC) #vazio - empty






