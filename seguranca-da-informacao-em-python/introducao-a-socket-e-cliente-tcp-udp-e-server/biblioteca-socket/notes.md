# Biblioteca Socket

### Definição

* Fornece acesso de baixo nível à interface de rede

* o OS fornece a API socket que relaciona o programa com a rede

### TCP

* **Definição**

  * É um dos protocolos de comunicação

  * Fornece suporte a rede global internet através da verificação da integridade dos dados (enviados na sequência correta e sem erros) 

  * **Baseado no princípio de integridade**

### UDP

> UDP é um acrônimo para User Datagram Protocol (Protocolor de Daragrama de Usuário)

* **Definição**

  * É um protocolo simples da camada de transporte

  * Responsável por permitir uma aplicação enviar um datagrama dentro de uma pacote IPv4 ou IPv6

  * **OBS**: não há garantia da chegada do pacote de forma íntegra em seu destino

  * **Não respeita o princípio da integridade, mas sim, o princípio da disponibilidade**