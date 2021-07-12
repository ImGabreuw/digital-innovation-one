# O que é a biblioteca Random, um hash e Multithreading?

### Biblioteca Random

* É uma implementação de geradores de números pseudoaleatórios para várias distribuições

* Baseado nos princípios de **autenticação** e **confidencialidade**

### Hash

* É um **identificador único**

* Pode ser gerado através de um algoritmo

  > **Algoritmo** (responsável por encriptar e desencriptar) = analisar *byte* a *byte* de um arquivo > gerar um código único (**hash**)

* Ao alterar 1 único *bit* do arquivo, o hash será completamente diferente

* Baseado no princípio de **integridade**

* Tipos de **hash**

  * md5
  * SHA1
  * SHA256
  * SHA512

* **Biblioteca hashlib**: É uma implementação de uma interface comum para muitos algoritmos de **hash** seguro (SHA1, SHA256, MD5, ...)

### Multithreading

* **Thread**: é **um processo**

* **Multithread**: é **um processo** que pode **responder várias solicitações** concorrentemente ou simultaneamente

* **Biblioteca threading**: construção de interfaces de alto nível para processamento usando o módulo Thread da biblioteca, de mais baixo nível (relação direta com o processador)

### Biblioteca ipaddress

* É possível **criar/manipular endereços IP** do ipo IPv4, IPv6 e redes inteiras