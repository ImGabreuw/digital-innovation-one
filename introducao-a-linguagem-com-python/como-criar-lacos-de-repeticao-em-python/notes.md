# Como criar laços de repetição em Python

### Sintaxe

* **Laço de repetição `for` com range**

  * **Sintaxe**

    ```python
    for <nome da variável> in range(<quantidade do números>):
        # Código
    ```

    > No caso acima, a contagem sempre começa em 0

    ```python
    for <nome da variável> in range(<início>, <fim>):
        # Código
    ```

  * **Exemplo**

    ```python
    for x in range(100):
      print(x) # 0 até 99
    ``` 

    ```python
    for x in range(1, 100):
      print(x) # 1 até 99
    ```

    ```python
    a = int(input("Entre com um número: "))

    div = 0

    for x in range(1, a + 1):
        resto = a % x

        if resto == 0:
            div += 1

    if div == 2:
        print("número {} é primo".format(a))
    else:
        print("número {} não é primo".format(a))
    ```

* **Laço de repetição `for` dentro de outro**

  * **Sintaxe**

    ```python
    for <expressão>:
      for <expressão>:
        # Código
    ```

  * **Exemplo**

    ```python
    intervalo = int(input("Entre com um valor: "))

    for num in range(intervalo + 1):
        div = 0

        for x in range(1, num + 1):
            resto = num % x

            if resto == 0:
                div += 1

        if div == 2:
            print(num)
    ```

* **Laço de repetição `while`**

  * **Sintaxe**

    ```python
    while <condição>:
      # Código
    ```

    > **CUIDADO**: caso a variável dentro da condição não for incrementada, esse **loop se torna infinito**

  * **Sintaxe**

    ```python
    a = 0
    while a < 10:
      print(a)
      a += 1
    ```