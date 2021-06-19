# mv - Mover arquivos

* **mv** = (M)o(V)e

* **Função**: mover e remover arquivos e diretórios

* **Uso**

  * `$ mv -i <arquivo/diretórios> <arquivo/diretórios>` = confirmar antes de substituir

  * `$ mv -n <arquivo/diretórios> <arquivo/diretórios>` = sem substituição

  * `$ mv -b <arquivo/diretórios> <arquivo/diretórios>` = substituir pelo backup

  * `$ mv -u <arquivo/diretórios> <arquivo/diretórios>` = substituir se o arquivo de destino for antigo ou não existir

* **Exemplo**

  * `$ mv -i teste.txt testes`

  * `$ mv -n teste.txt testes`

  * `$ mv -b teste.txt testes`

  * `$ mv -u teste.txt testes`