
def mensagem():
    print("Olá")

mensagem()


def calcular(num1, num2):
	print(num1+num2)
        
calcular(2,2)

# RETURN

print(mensagem()) #None - pq não tem return


def calcular2(num1, num2):
	return num1+num2

print (calcular2(10,3))


# Retornando mais de um valor!

def exibir(num1, num2):
	return num1, num2  #retorna uma Tupla (por ser imutável)

print(exibir(4,5)) 



#### PASSANDO ARGUMENTOS DE OUTRA FORMA ####

print(exibir(num1=3, num2=100))  # evita erro caso troquem a ordem dos parâmetros na função


# ARGS E KWARGS

def definir_poema(data, *args, **kwargs):
	texto = "\n".join(args)
	infos = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
	mensagem = f"{data}\n\n{texto}\n\n{infos}"
	print(mensagem)


definir_poema(
	"25 de julho de 2022",
	"Rosas são como o amanhã.",
	"Cheias de cor e paixão",
	autor="Luiz Burn",
	ano=2018
)

# POSITION ONLY

def criar_carro1(ano, modelo, placa, /, marca):
	print(ano, modelo, placa, marca)

criar_carro1(1999, "Palio", "EUS9876", "Fiat")


# KEYWORD ONLY

def criar_carro2(*, ano, modelo, placa, marca):
	print(ano, modelo, placa, marca)

criar_carro2(ano=1999, modelo="Palio", placa="EUS9876", marca="Fiat")


# POSITION AND KEYWORD

def criar_carro3(*, ano, modelo, placa, marca):
	print(ano, modelo, placa, marca)

criar_carro3(ano=1999, modelo="Palio", placa="EUS9876", marca="Fiat")


#### OBJETOS DE PRIMEIRA CLASSE ####

def somar(a,b):
	return a + b

def exibir(a, b, funcao):
	result = funcao(a,b)
	print(f"{a} + {b} = {result}")

exibir(10,10,somar)


# Atribuindo função a uma variável

fun_var = somar

print(fun_var(3,4))



# ESCOPO GLOBAL E LOCAL

salario = 2000

def salario_calc(bonus):
	global salario
	salario += bonus
	return salario

print(f"Salário final: R$ {salario_calc(500)}")