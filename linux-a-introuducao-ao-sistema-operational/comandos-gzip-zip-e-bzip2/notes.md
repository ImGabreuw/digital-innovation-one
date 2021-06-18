# Comandos gzip, zip e bzip2

### Compactadores

* São programas que diminuem o tamanho de um arquivo ou diretório

* **gzip** (**compactação**)

  * **Características**

    * Compactador muito usado

    * Alta taxa de compactação

  * **Uso**: 

    * Compactação normal: `$ gzip <arquivo>`

    * Compactação máxima: `$ gzip -9 <arquivo>`

  * **Exemplo**: 
    
    * `$ gzip teste.txt`

    * `$ gzip -9 teste.txt`

* **gunzip** (**descompactação**)

  * **Uso**: `$ gunzip <arquivo compactado>`

  * **Exemplo**: `$ gzip teste.txt.gz`

* **zip** (**compactação**)

  * **Uso**: `$ zip <nome do arquivo após a compactação> <arquivo>`

  * **Exemplo**: `$ zip teste.zip teste.txt`

* **unzip** (**descompactação**)

  * **Uso**: `$ unzip <arquivo compactado>`

  * **Exemplo**: `$ zip teste.zip`

* **bzip2** (**compactação**)

  * **Características**

    * Compactador mais atual

  * **Uso**: `$ bzip2 <arquivo>`

  * **Exemplo**: `$ bzip2 teste.txt`

* **bzip2** (**descompactação**)

  * **Uso**: `$ bzip2 -d <arquivo compactado>`

    > **-d** = (D)escompactar

  * **Exemplo**: `$ bzip2 -d teste.bz2`
    
### Extensões

* Identificam o tipo de um arquivo e o programa necessário para manipular o mesmo

* Um arquivo ao ser compactado é adicionados, ao final do nome, uma extensão

* **Exemplo**

  * Arquivo compactado pelo programa rar, recebe a extensão `.rar`

  * Arquivo compactado pelo programa zip, recebe a extensão `.zip`

* Ao descompactar, a extensão é removida do arquivo