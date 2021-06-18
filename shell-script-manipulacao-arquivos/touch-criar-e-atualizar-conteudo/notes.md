# touch - Criar e atualizar o conteúdo

* **Função** = criar arquivos vazios ou alterar data e hora do arquivo

* **Uso**

  * `$ touch <arquivo(s)>` = criar múltiplos arquivos

  * `$ touch -a <arquivo>` = alterar hora de acesso

  * `$ touch -m <arquivo>` = alterar hora da modificação

  * `$ touch -c <arquivo>` = alterar hora de acesso sem criar um novo arquivo

  * `$ touch -t <hora> <arquivo>` = definir hora específica de acesso e modificação 

    * Padrão de hora: 
      
      * **Formato**: `CCYYMMDDhhmm.ss`

        * **CC** = os dois primeiros dígitos do ano

        * **YY** = os dois dígitos subsequentes do ano

        * **MM** = mês

        * **DD** = dia

        * **hh** = hora

        * **mm** = minuto

        * **ss** = segundo

      * **Exemplo**: `202012081047.30`

* **Exemplos**

  * `$ touch arquivo1.txt arquivo2.txt arquivo3.txt`

  * `$ touch -a arquivo.txt`

  * `$ touch -m arquivo.txt`

  * `$ touch -c arquivo.txt`

  * `$ touch -t 202012081047.30 arquivo.txt`