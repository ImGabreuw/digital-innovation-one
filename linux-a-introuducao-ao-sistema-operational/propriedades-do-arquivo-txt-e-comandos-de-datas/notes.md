# Propriedades do arquivo .txt e comandos de datas

### Comandos de datas

* `$ head <nome do arquivo>`

  * Mostrar as 10 primeiras linhas de um arquivo

  * **Exemplo**: `$ head teste.txt`

* `$ head <nome do arquivo> > <nome do novo arquivo>`

  * Mover as 10 primeiras linhas para um outro arquivo

  * **Exemplo**: `$ head teste.txt > distro.txt`

* `$ tail <nome do arquivo>`

  * Mostrar as 10 últimas linhas de um arquivo

  * **Exemplo**: `$ tail teste.txt>`

* `$ tail <nome do arquivo> > <nome do novo arquivo>`

  * Mover as 10 últimas linhas para um outro arquivo

  * **Exemplo**: `$ tail teste.txt > distro.txt`

* `$ tail <nome do arquivo> | grep <texto>`

  * Buscar por um texto dentro do arquivo

  * **Exemplo**: `$ tail distro.txt | grep Linux`

* `$ cal > <nome do arquivo>` 

  * Mover o resultado de um comando para um arquivo

  * **Exemplo**: `$ cal > calendario_jul.txt`

* `$ date`

  * Exibir a data atual

  * **Exemplo** `$ date`

* `$ date >> <nome do arquivo existente>`

  * Adicionar a data atual (ou outro resultado) no final de um arquivo

  * **Exemplo**: `$ date >> calendario_jul.txt`