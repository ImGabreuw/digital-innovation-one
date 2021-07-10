# O que é Ping?

### ICMP

> ICMP é um acrônimo para (I)nternet (C)ontrol (M)essage (P)rotocol

* **Definição**: é um protocolo integante do **Protocolo IP** utilizado para fornecer relatórios de erros à fonte original

### Ping

* **Definição**

  * É uma ferramenta que usa o protocolo ICMP para testara conectividade entre **nós** (qualquer ponto em uma rede)

  * É um comando disponível praticamente em todos os Sistema Operacional

  * Consiste no envio de pacotes (_request_) para o equipamento de destino e na "escuta" das respostas (_reply_) -> verificação do status de um nó

  * **Contempla o princípio da disponibilidade**

* **Representação**

  ![](./assets/representacao-ping.png)

* **Comando `ping`**

  * **Enviar infinitas requisições**: `$ ping www.google.com`

    > Para interromper os envios, pressione: `CTRL + C`

  * **Enviar um número definido de requisições**: `$ ping -c 6 www.google.com`

### Biblioteca OS do Python

* Maneira simples de utilizar funcionalidades do Sistema Operacional 