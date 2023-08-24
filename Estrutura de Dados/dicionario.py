

pessoa = {"nome": "Guilherme", "idade": 28}

print(pessoa["nome"])
print(pessoa)


pessoa["nome"] = "Luiz"

print(pessoa["nome"])

# Rodando e exibindo de forma confiável
for chave, valor in pessoa.items():
    print(chave, valor)


# MÉTODOS

nomes = pessoa.copy()
print(nomes)


thisdict  = dict.fromkeys(["profissão", "cor"], "Ator")  #add com valor
print(thisdict)

print(pessoa.get("nome"))


print(pessoa.items())

print(pessoa.keys())

print(pessoa.values())

print(pessoa.pop("cor", "Não existe")) #retorna o texto se não achar a chave

print(pessoa.popitem()) #tira o primeiro par
print(pessoa)


pessoa.setdefault("nome", "Michael") #nome já existe, não vai adicionar nem alterar
pessoa.setdefault("altura", 1.75) #não existe, será add ao dicionário
print(pessoa)

print("nome" in pessoa) #True
print("peso" in pessoa) #False

del pessoa["nome"]
print(pessoa)


# ANINHANDO DICIONÁRIOS

contato = {
	"felipeksid@yahoo.com": {"nome": "Fellipe", "idade": 22},
	"andreacampos@gmail.com": {"nome": "Andréa", "idade": 51, "sobrenome": {"primeiro": "Campos"}}
}

print(contato["felipeksid@yahoo.com"]["nome"])
print(contato["andreacampos@gmail.com"]["sobrenome"]["primeiro"])