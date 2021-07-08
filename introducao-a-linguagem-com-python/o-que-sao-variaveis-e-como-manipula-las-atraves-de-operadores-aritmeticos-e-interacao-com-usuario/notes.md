# O que são variáveis e como manipulá-las através de operadores aritméticos e interação com usuário

### Sintaxe dp Python

* **Verificar o tipo da variável**

  * **Sintaxe**

    ```python
    type(<variável>)
    ```

  * **Exemplo**

    ```python
    a = 5
    print(type(a)) # <class 'int'>
    ```

* **Comentário**

  ```python
  # Aqui é um comentário
  ```

* **Converter um número para String**

  * **Sintaxe**

    ```python
    str(<variável/número>)
    ```

  * **Exemplo**

    ```python
    a = 6
    a = str(a)
    print(a) # 15
    print(type(a)) # <class 'str'>

    ```

* **Concatenação de Strings**

  * **Sintaxe**

    ```python
    "Texto" + <variável do tipo String>
    ```

  * **Exemplo**

    ```python
    soma = 5 + 5
    print("Soma = " + str(soma)) # Soma = 10
    ```

* **Casas decimais e arredondamento**

  * **Sintaxe**

    ```python
    int(<variável/número com casas decimais>)
    ``` 

  * **Exemplo**

    ```python
    divisao = 10 / 5
    print(type(divisao)) # <class 'float'>
    print("Com casa decimal: " + str(divisao)) # Com casa decimal: 2.0
    print("Sem casa decimal: " + str(int(divisao))) # Sem casa decimal: 2
    ```

* **Formatação de Strings**

  * **Sintaxe**

    ```python
    print("Texto {}".format(1)) # Texto 1
    print("Texto {} {}".format(1, 2)) # Texto 1 2
    ```

    > Cada `{}` é uma valor que será passado como argumento da função `format()`

  * **Exemplo**

    ```python
    soma = 5 + 5
    print("Soma: {}".format(soma))
    ```
  
* **Formatação de Strings com alias**

  * **Exemplo**

    ```python
    "Texto {<alias>}".format(<alias>=<valor>)
    ```

  * **Exemplo**

    ```python
    print("Valor: {valor}".format(valor=1)) # Valor: 1
    print("Valores: {valor1} {valor2}".format(valor1=1, valor2=2)) # Valor: 1, 2
    ```

* **"Quebra de linha"**

  * **Sintaxe**: `\n`

  * **Exemplo**

    ```python
    print(
        "Linha 1"
        "\nLinha 2"
        "\nLinha 3"
    )

    # Saída:
    # Linha 1
    # Linha 2
    # Linha 3
    ```

* **Interação com o usuário**

  * **Sintaxe**

    ```python
    input()
    ```

    **OU**

    ```python
    input("Esse texto será exibido no terminal para o usuário")
    ```

    > **IMPORTANTE**: o retorno da função `input()` é sempre do tipo String (**str**)

  * **Exemplo**

    ```python
    a = input("Entre com o primeiro valor: ") # "$ Entre com o primeiro valor: 10"
    print(type(a)) # <class 'str'>
    ```