# Instalação, atualização e remoção de pacotes

### Pacotes

* São programas colocados dentro de um arquivo identificados por sua extensão

* Nele incluem arquivos necessários para a atualização do programa

* Extensões de pacotes

  * `.dev` (mais utilizado)

  * `.rpm`

### Gerenciadores de pacotes

* São sistemas que possuem 
  
  * Resolução automática de dependências entre pacotes

  * Método fácil de instalação de pacotes

* **Exemplos**

  * **dpkg**

  * **apt**

  * **yum**

  * **rpm**

### apt

* Gerenciador de pacotes mais utilizado

* **Instalação**

  * **Uso**: `$ sudo apt install <pacote>`

  * **Exemplo**: `$ sudo apt install nmap`

* **Atualização**

  * **Uso**: `$ sudo apt upgrade <pacote>`

  * **Exemplo**: `$ sudo apt upgrade nmap`

* **Remoção**

  * **Uso**: `$ sudo apt remove <pacote>`

  * **Exemplo**: `sudo apt remove nmap`