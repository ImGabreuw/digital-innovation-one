# Comandos hostname e ping

### Comando **hostname**

* `$ hostname` = nome do computador

* `$ hostname -I` = endereço do computador da rede local

* `$ hostname -i` = endereço de loopback do computador

* `$ who` = informações de conexão na rede

* `$ whoami` = nome do usuário conectado à rede

* `$ ping <url> <limite, em segundos>`
  
  * Pertence ao **Protocolo ICMP**

  * Verificar se o host está ativo

  * **Funcionamento**: envia um _ping_ (pacote de requisição) para o host e recebe as respostas (_pong_)

  * **Exemplo**

    * `$ ping www.google.com`

    * `$ ping www.google.com -w 10`

* `dig <url>`

  * Informações de DNS