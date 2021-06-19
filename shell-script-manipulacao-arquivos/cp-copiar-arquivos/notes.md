# cp - Copiar arquivos

* **cp** = (C)o(P)y

* **Função**: copiar arquivos ou diretórios para outro local

* **Características**

  * Sem confirmação de existência ou não, exceto se usar a flag `-i`

    > **-i** = (I)nterativa

  * Nenhuma saída será exibida, exceto se usar a flag `-v`

    > **-v** = (V)erbose

* **Uso**

  * `$ cp -i <arquivo/diretório> <diretório>` = criar _hard links_ em vez de copiar os arquivos


  * `$ cp -s <arquivo/diretório> <diretório>` = criar _links simbólicos_ em vez de copiar arquivos

  * `$ cp -u <arquivo/diretório> <diretório>` = copiar apenas quando o arquivo de origem for mais novo do que o arquivo de destino ou quando o arquivo de destino não existir