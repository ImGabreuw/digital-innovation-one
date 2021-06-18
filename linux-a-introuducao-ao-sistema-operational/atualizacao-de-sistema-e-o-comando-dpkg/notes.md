# Atualização de sistema e o comando dpkg

### Atualização do Sistema

* Utilização do **apt**

  * **Importante**: é necessário a utilização do usuário _root_ para o funcionamento desse comando

  * **Uso**: 
    
    * `$ sudo su`

    * `$ apt update && apt upgrade`

  * **Exemplo**: `$ sudo apt update && apt upgrade`

### Sites de pacotes

* [pkgs](https://pkgs.org/)

* [rpm.pbone](http://rpm.pbone.net/)

### Instalação

* dpkg

  * **Instalação**

    * **Características**

      * Instalador de pacotes deb

    * **Uso**: `$ sudo dpkg -i <pacote>`

      > **-i** = (I)nstall

    * **Exemplo**: `$ sudo dpkg -i docker-ce-cli_amd64.deb`

  * **Informações**

    * **Função**: Obter a descrição do pacote

    * **Uso**: `$ sudo dpkg -I <pacote deb>`

    * **Exemplo**: `$ sudo dpkg -I docker-ce-cli_amd64.deb | more`

  * **Remoção**

    * **Função**: remover um pacote deb ap a partir do nome

      > Para obter o nome do pacote é necessário utilizar o comando `$ sudo dpkg -I <pacote deb>` e buscar pela chave **Package** (**Exemplo**: `Package: docker-ce-cli`)

    * **Uso**: `$ sudo dpkg -r <pacote>`

      > **-r**: (R)emove

    * **Exemplo**: `$ sudo dpkg -r <pacote>`

