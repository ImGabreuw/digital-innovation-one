# Comandos traceroute e finger

### Instalação do **traceroute**

* `$ sudo apt install traceroute`

### Instalação **whois**

* `$ sudo apt install whois`

### Instalação **finger**

* `$ sudo apt install finger`

### traceroute

* `$ traceroute <url>`

  * Informações sobre os nós que existe até o domínio

  * **Exemplo**: `$ traceroute www.google.com`

* `$ dig <url> +short`

  * Mostrar apenas o IP DNS de um domínio

  * **Exemplo**: `$ dig www.google.com +short`

### whois

  * Obter mais informação sobre um domínio da internet

  * **Exemplo**: `$ whois www.pudim.com.br`

### finger

  * Mostrar as informações do usuário logado na host local

  * **Exemplo**: `$ finger`