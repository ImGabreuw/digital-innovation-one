# Como criar um código em Python que funcione de acordo com a relação das variáveis

### Links úteis

* [devmedia](https://www.devmedia.com.br/operadores-no-python/40693)

### Sintaxe

* **Condicional `if`**

  * **Sintaxe**

    ```python
    if <condição>:
      # Código se a condição for verdadeira
    ```

    > A indentação (4 espaços) é muito importante no Python, pois ela indica o começo e o fim da condicional, função, etc

  * **Exemplo**

    ```python
    a = 5
    b = 4

    if a > b:
      print("{} é maior que {}".format(a, b))
    ```

* **Condicional `if-else`**

  * **Sintaxe**

    ```python
    if <condição>:
      # Código se a condição for verdadeira
    else:
      # Código se a condição for false
    ```

  * **Exemplo**

    ```python
    a = 5
    b = 4

    if a > b:
      print("{} é o maior número".format(a))
    else:
      print("{} é o maior número".format(b))
    ```

* **Encadeamento de `if-else` (elif)**

  * **Sintaxe**

    ```python
    if <condição>:
      # Código se a condição for verdadeira
    elif <condição>:
      # Código se a condição for verdadeira
    else:
      # Código se todas as condições anteriores foram falsas
    ```

  * **Exemplo**

    ```python
    a = 10
    b = 5
    c = 20

    if a > b and a > c:
        print("O maior número é {}".format(a))
    elif b > a and b > c:
        print("O maior número é {}".format(b))
    else:
        print("O maior número é {}".format(c))

    print("Final do programa")
    ```

* **Operador lógico: `==` (igualdade)**

  * **Sintaxe**

    ```python
    <valor1> == <valor2>
    ```

  * **Exemplo**

    ```python
    a = 10
    resto = a % 2

    if resto == 0:
        print("O número {} é par.".format(a)) # <-- Saída
    else:
        print("O número {} é ímpar.".format(a))
    ```

* **Operador lógico: `or` (ou)**

  * **Sintaxe**

    ```python
    <condição 1> or <condição 2>
    ```

  * **Exemplo**

    ```python
    a = 15
    b = 10
    resto_a = a % 2
    resto_b = b % 2

    if resto_a == 0 or resto_b == 0:
        print("Foi digitado um número par") # <-- Saída
    else:
        print("Não foi digitado um número par")
    ```

* **Operador lógico: `not` (negação)**

  * **Sintaxe**

    ```python
    <condição 1> or not <condição 2>
    ```

  * **Exemplo**

    ```python
    a = 15
    b = 10
    resto_a = a % 2
    resto_b = b % 2

    if resto_a == 0 or not resto_b > 0:
        print("Foi digitado um número par") # <-- Saída
    else:
        print("Não foi digitado um número par")
    ```