class Calculadora:

    def soma(self, num1, num2):
        return num1 + num2

    def subtracao(self, num1, num2):
        return num1 - num2

    def multiplicacao(self, num1, num2):
        return num1 * num2

    def divisao(self, num1, num2):
        return num1 / num2


calculadora = Calculadora()

print(calculadora.soma(10, 2))
print(calculadora.subtracao(5, 3))
print(calculadora.multiplicacao(100, 2))
print(calculadora.divisao(20, 4))
