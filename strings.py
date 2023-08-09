nome = "fElLiPe"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá, tenho espaços!  "

print(texto)
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

print(".".join(nome))
print(nome.center(12, "#"))
print(nome.center(12))

###  INTERPOLAÇÕES  ###

idade = 22
profissao = "Programador"
PI = 3.14159

print(f"Olá, meu nome é {nome}, tenho {idade} anos e atuo como {profissao}")

print(f"Valor de PI: {PI:.2f}")
print(f"Valor de PI: {PI:10.2f}") #acrescenta espaços até preencher 10 caracteres

print("Olá, meu nome é %s, tenho %i anos e atuo como %s" % (nome, idade, profissao))

print("Olá, meu nome é {}, tenho {} anos e atuo como {}".format(nome, idade, profissao))

print("Olá, meu nome é {1}, tenho {2} anos e atuo como {0}".format(profissao, nome, idade))


##  FATIAMENTO ##

print(profissao[0])
print(profissao[-4])

print(profissao[:5])
print(profissao[3:])

print(profissao[1:4])
print(profissao[1:4:2])

print(profissao[:])
print(profissao[::-1])


## STRINGS MÚLTIPLAS LINHAS / TRIPLAS ##

mensagem = f"""
    Olá, meu nome é {nome}
        Prazer em te conhecer
"""

print(mensagem)