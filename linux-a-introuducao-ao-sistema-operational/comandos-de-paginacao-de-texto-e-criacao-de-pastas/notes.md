# Comando de paginação de textos e criação de pastas

### Comando de paginação de textos

* `| more`

  * paginação de textos

  * **Exemplo**: `$ cat teste.txt | more`

* `| less`

  * paginação de textos

  * **Exemplo**: `$ cat teste.txt | less`

* `&`

  * Operador de redirecionamento

  * Cada comando será executado em linhas de comandos separadas

  * **Exemplo**: `$ cat maio.txt & cat junho.text`

* `&&`

  * Operador de redirecionamento

  * Todos os comandos serão executados em uma única linhas de comandos

  * **Exemplo**: `$ cat maio.txt & cat junho.text`

### Criação de pastas

* Criar um diretório e entrar nele

  * `$ mkdir <diretório> && cd <diretório>`

  * **Exemplo**: `$ mkdir linux_ubuntu && cd linux_ubuntu`

* Exibir o tipo de um arquivo/diretório

  * `$ file <nome do arquivo/diretório>`

  * **Exemplo**: 
  
    * `$ file maio.txt`
    * `$ file linux_ubuntu`

* Exibir qual a funcionalidade de um comando

  * `$ whatis <comando>`

  * **Exemplo**: `$ whatis file`

* Buscar um arquivo dentro de um diretório

  * `$ find <diretório> -name <nome do arquivo>`

  * **Exemplo**: `$ find ~ -name maio.txt`