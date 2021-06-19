# find - Procurar por arquivos e rm - Removendo arquivos

* **Função** = procurar arquivos

* **Uso**: 
  
  * `$ find .` = pesquisar todos os arquivos do diretório atual

  * `$ find <diretório> -type f -name "<nome do arquivo>"` = buscar apenas pelos arquivos com o nome especificado no comando 

    > **-type** = f = (F)ile

  * `$ find <diretório> -type d -name "<nome do diretório>"` = buscar apenas pelos diretórios com o nome especificado no comando 

    > **-type** = d = (D)irectory

  * `$ find <diretório> -type d -name "<iniciais do diretório>*"` = buscar todos os diretórios com as iniciais especificadas no comando

* **Exemplo**

  *  `$ find .`

  * `$ find ./ -type f "teste.txt"`

  * `$ find ./ -type d -name "testes"`

  * `$ find ./ -type d -name "tes*"`