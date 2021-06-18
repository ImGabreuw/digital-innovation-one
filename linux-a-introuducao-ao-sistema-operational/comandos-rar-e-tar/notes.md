# Comandos rar e tar

### Compactadores

* **rar** (**compactação**)

  > Necessita ser instalado

  * **Uso**: `$ rar a <nome do arquivo após ser compactado> <arquivo>`

    > **a** = (A)ção de compactar

  * **Exemplo**: `$ rar a teste.rar teste.rar`

* **rar** (**descompactação**)

  * **Uso**: `$ rar x <arquivo>`

  * **Exemplo**: `$ rar x teste.rar`

### Arquivadores

* Responsável por juntar vários arquivos em um só

* Pode ser usado em conjunto com um compactador para armazenar arquivos compactados

* **tar** (**compactação**)

  * **Características**

    * Arquivador muito utilizado no Linux (usado até em arquivos do sistema)

  * **Uso**: `$ tar -cf <nome do arquivo após o arquivamento> <arquivo(s)>`

  * **Exemplo**: 
  
    * Arquivar: `$ tar -cf testes.tar teste1.txt teste2.txt`

    * Compactar: `$ gzip testes.tar`

* **tar** (**descompactação**)

  * **Uso**: 
  
    * Extrair para o diretório atual: `$ tar -xvf <arquivo compactado>`

    * Extrair para outro diretório: `$ tar -xvf <arquivo compactado> -C <diretório>`

  * **Exemplo**: 
    
    * `$ tar -xvf testes.tar.gz`

    * `$ tar -xvf testes.tar.gz -C ~/Documentos`


