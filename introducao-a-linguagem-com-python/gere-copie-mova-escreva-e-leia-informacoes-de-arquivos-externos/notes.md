# Gere, copie, mova, escreva e leia informações de arquivos externos

### Manipulação de arquivos

* **Criar um arquivo**

  * **Sintaxe**

    ```python
    open("nome do arquivo + extensão", "w")
    ```

    > `w` = (w)rite, ou seja,  é a opção para escrever o arquivo

  * **Exemplo**

    ```python
    open("teste.txt", "w")
    ```

* **Escrever em um arquivo**

  * **Sintaxe**

    ```python
    variavelArquivo.write("texto")
    variavelArquivo.close() # Boa prática
    ```

    > OBS: o método `write()` substitui o conteúdo anterior, se tiver, pelo novo (passado no argumento)

  * **Exemplo**

    ```python
    arquivo = open("teste.txt", "w")
    arquivo.write("Minha primeira escrita")
    arquivo.close()
    ```

* **Escrever em um arquivo existente**

  * **Sintaxe**

    ```python
    arquivo = open("nome do arquivo + extensão", "a")
    arquivo.write("texto")
    arquivo.close()
    ```

  * **Exemplo**

    ```python
    arquivo = open("teste.txt", "a")
    arquivo.write("Minha primeira escrita\n") # "\n" = quebra de linha
    arquivo.close()
    ```

* **Ler o conteúdo de um arquivo**

  * **Sintaxe**

    ```python
    arquivo = open("nome do arquivo + extensão", "r")
    arquivo.read()
    ```

  * **Exemplo**

    ```python
    arquivo = open(nome_arquivo, "r")
    texto = arquivo.read()
    print(texto)
    ```

* **Copiar um arquivo**

  * **Sintaxe**

    ```python
    import shutil
    shutil.copy("arquivo", "destino")
    ```

  * **Exemplo**

    ```python
    import shutil
    shutil.copy("teste.txt", ".")
    ```

* **Mover um arquivo**

  * **Sintaxe**

    ```python
    import shutil
    shutil.move("arquivo", "destino")
    ```

  * **Exemplo**

    ```python
    import shutil
    shutil.move("teste.txt", ".")
    ```