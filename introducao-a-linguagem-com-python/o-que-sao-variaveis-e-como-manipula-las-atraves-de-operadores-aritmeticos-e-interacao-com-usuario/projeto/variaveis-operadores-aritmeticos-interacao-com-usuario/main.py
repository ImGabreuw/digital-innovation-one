a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))

soma = a + b
# print("Soma:" + soma) -> Erro: tipos incompatíveis, int e str
# soma = str(soma)
# print("Soma: " + soma)
print("Soma: {}".format(soma))
print(type(soma))

subtracao = a - b
print(subtracao)

multiplicacao = a * b
print(multiplicacao)

divisao = a / b
tipo = type(divisao)
sem_casa_decimal = int(divisao)
print(
    "Tipo: {tipo}"
    "\nCom casa decimal: {com_casa_decimal}"
    "\nSem casa decimal: {sem_casa_decimal}"
        .format(tipo=tipo, com_casa_decimal=divisao, sem_casa_decimal=sem_casa_decimal)
)

resto = a % b
print(resto)
