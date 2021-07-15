# Manipulando dados com Shell Script

### Linux

* *case-sensitive*

* Sistema orientado a objetos

### IMPORTANTE

* Estruturação das pastas (cada pasta com uma responsabilidade)

### Comandos

* `$ pwd` = exibir o caminho do diretório atual

* `$ cat <arquivo>` = visualizar o conteúdo de um arquivo

* `$ ls -lhtr` = ?

* `$ ls -htr` = ?

* `$ ll` = ?

* `$ bc` = ?

* `$ awk` = ?


### Shell Script

* **Variáveis**

    * **Declarar uma variável**

      ```shell
      NOME_ARQUIVO=teste
      ```

    * **Chamar uma variável** 

      ```shell
      ${NOME_ARQUIVO}
      ```

* Comentários (`#`) é essencial

* **Executar um *shell script***: `$ sh <arquivo>`

* **Comandos**

  * `$ echo <valor>` = imprimir um valor na tela do terminal

  * `$ echo <valor> > <arquivo>` (**`>`**) = inserir um valor ou saída de um comando em um novo arquivo

  * `$ echo <valor> >> <arquivo>` (**`>>`**) = inserir um valor ou saída de um comando em um arquivo existente (caso esse arquivo não exista, será criado um novo)

  * `|` = executar um comando com base na saída do comando anterior

  * `$ wc` = contagem

    > A flag `-c` indica a contagem de caractéres

  * **Utilização de crase em palavras reservados do Linux**
    
    * Sem crase: var=ls -> executar o comando `$ ls`, ou seja, a listagem dos arquivos e diretórios

    * Com crase: var=`ls` -> armazenar o resultado do comando `ls` em uma variável

  * `$ ls -tr` = listagem por tempo reverso

    * Flag `-t` = ordenar por tempo

    * Flag `-r` = reverter uma ordenação

  * `?` <=> **1 caractere** qualquer

  * `$ head -<número>` = cabeçalho de uma "lista"

    > Exemplo: `$ head -1` -> exibir o primeiro elemento de uma listagem

  * `$ tail -<número>` = calda de uma lista

    > Exemplo: `$ tail -1` -> exibir o último elemento de uma listagem

  * `$ cut <início>-<fim>` = ?

  * `\<caractere>` = exibir o caractere após a barra invertida