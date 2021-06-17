# Comandos history, alias e outras interações com arquivos .txt

### Comando **history**

* Limpar o histórico de comandos do terminal: `$ history -c`

### Comando **alias**

* nickname/sinônimo para um comando: `$ alias <sinônimo>='<comando>'`

* Exemplo: `$ alias hh='history'`

### Outros comandos

* `$ nl <arquivo>`

  * Numerar as linhas (**exceto as em branco**) de um arquivo texto

  * **Exemplo**: `$ nl teste.txt`

* `$ wc -l <arquivo>`

  > **-l** = _lines_

  * Numerar as linhas (**inclusive as em branco**) de um arquivo texto

  * **Exemplo**: `$ wc -l teste.txt`

* `$ wc -w <arquivo>`

  > **-w** = _words_

  * Exibir o número de palavras de um arquivo texto

  * **Exemplo**: `$ wc -w teste.txt`

* `$ cmp <arquivo> <arquivo>`

  * Comparar 2 arquivos

  * **Exemplo**: `$ cmp teste1.txt teste2.txt`

* `$ diff <arquivo> <arquivo>`

  * Mostrar o arquivo que não está vazio

  * **Exemplo**: `$ diff teste1.txt teste2.txt`

* `$ sort -n <arquivo>`

  * organizar a saído do arquivo em ordem numérica

  * **Exemplo**: `$ sort -n teste.txt`