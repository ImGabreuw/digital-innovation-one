# Construindo métodos, funções e classes em Python

### Função VS método

* Para declarar uma função ou método, usa-se a palavra reservada: `def`

* **OBS**

  * Função é tudo que retorna um valor

  * Método é tudo que não possui retorno

* **Exemplo de função**

  ```python
  def soma(a, b):
    return a + b
  ```

* **Exemplo de método**

  ```python
  def soma(a, b):
    print(a + b)
  ```

### Classe 

* **Para declarar uma classe, usa-se a palavra reservada: `class`**

  * **Sintaxe**

    ```python
    class NomeDaClasse:
      # Código
    ```  

  * **Exemplo**

    ```python
    class Calculadora:

      def soma(a, b):
          return a + b

      def subtracao(a, b):
          return a - b

      def multiplicacao(a, b):
          return a * b

      def divisao(a, b):
          return a / b
    ```

* **Toda classe necessita de um método `__init__`, ou seja, é como um "construtor"**

  * **Sintaxe**

    ```python
    class NomeDaClasse:

      def __init__(self, parâmetros, ...):
        # Código
    ```

    > **`self`** é uma palavra reservada que serve para referênciar a classe, é como um "`this`"

  * **Exemplo**

    ```python
    class Calculadora:

      def __init__(self, num1, num2):
          self.num1 = num1
          self.num2 = num2

      def soma(self):
          return self.num1 + self.num2

      def subtracao(self):
          return self.num1 - self.num2

      def multiplicacao(self):
          return self.num1 * self.num2

      def divisao(self):
          return self.num1 / self.num2
    ```

    ```python
    class Calculadora:

      # def __init__(self):
      #    pass

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
    ```

    > **OBS**: o método `__init__` **NUNCA** pode ficar vazio (**se for declarado**), por isso usa-se `pass`. Caso a classe não tenha nenhum atributo, é possível omití-lo

* **Instanciar uma classe**

  * **Sintaxe**

    ```python
    NomeDaClasse()
    ```

  * **Exemplo**

    ```python
    calculadora = Calculadora(10, 2)
    ```

* **Acessar um função ou método de uma classe**

  * **Sintaxe**

    ```python
    nomeDaClasse.nomeDaFuncao()
    nomeDaClasse.nomeDoMetodo()
    ```

  * **Exemplo**

    ```python
    print(calculadora.soma()) # 12
    print(calculadora.subtracao()) # 8
    print(calculadora.multiplicacao()) # 20
    print(calculadora.divisao()) # 5.0
    ```

* **Acessar um atributo de uma classe**

  * **Sintaxe**

    ```python
    nomeDaClasse.nomeDoAtributo
    ``` 

  * **Exemplo**

    ```python
    class Televisao:

      def __init__(self):
          self.ligada = False

      def power(self):
          if self.ligada:
              self.ligada = False
          else:
              self.ligada = True


    televisao = Televisao()
    print("Televisão está ligada? {}".format(televisao.ligada)) # Televisão está ligada? False

    televisao.power()
    print("Televisão está ligada? {}".format(televisao.ligada)) # Televisão está ligada? True

    televisao.power()
    print("Televisão está ligada? {}".format(televisao.ligada)) # Televisão está ligada? False
    ```