# Comando chmod

### Exemplo 

* `$ chmod 200 teste.txt`

  * `200` (**Modo Octal**)

    * usuário dono = permissão de escrita (**2** = (W)rite)

    * grupo = sem permissão (**0**)

    * outros = sem permissão (**0**)

* `$ chmod 300 teste.txt`

  * `300` (**Modo Octal**)

    * usuário dono = permissão de execução (**1**) e escrita (**2**) (**2** + **1** = **3**)

    * grupo = sem permissão (**0**)

    * outros = sem permissão (**0**)

* `$ chmod 700 teste.txt`

  * `700` (**Modo Octal**)

    * usuário dono = permissão de leitura (**4**), escrita (**2**) e execução (**1**) (**4** + **2** + **1** = **7**)

    * grupo = sem permissão (**0**)

    * outros = sem permissão (**0**)

* `$ chmod 755 teste.txt`

  * `700` (**Modo Octal**)

    * usuário dono = permissão de leitura (**4**), escrita (**2**) e execução (**1**) (**4** + **2** + **1** = **7**)

    * grupo = permissão de leitura (**4**) e execução (**1**) (**4** + **1** = **5**)

    * outros = permissão de leitura (**4**) e execução (**1**) (**4** + **1** = **5**)