# O que são Redes, Protocolos e Interfaces de rede

### Fundamentos de rede

* O que é rede?

  * Rede de computadores é um conjunto de equipamentos interligados de maneira a trocarem informações e compartilharem recursos, por exemplo:

    * Arquivos de dados gravados

    * Impressoras

    * Modems

    * Softwares

  * Nós = pontos de rede, em uma casa, por exemplo:

    * Computadores

    * Celulares

    * Roteadores

* Rede WAN

  > **WAN** = (W)ide (A)rea (N)etwork ou (W)orld (A)rea (N)etwork

  * É uma rede geograficamente distribuída

* Rede MAN (Ramificação da rede WAN)

  > **MAN** = (M)etropolitan (A)rea (N)etwork

  * É uma rede metropolitana que interligam várias redes locais

  * Interligam redes locais

* Rede Lança

  > **LAN** = (L)ocal (A)rea (N)etwork

  * É uma rede local de uma forma geral em um único prédio ou campus

* **Protocolos**

  * É uma "linguagem" usada pelos dispositivos de uma rede de modo que eles consigam se entender

  * Existem vários protocolos

    * **IP**

      * Protocolo de Internet

      * Dentro desse protocolo possui o **endereço IP**

      * Números que identificam seu computador em uma rede

    * **ICMP**

      > **ICMP** = (n)ternet (C)ontrol (M)essage (P)rotocol

      * **Função**: prover mensagens de controle na comunicação entre nós

    * **DNS**

      > **DNS** = (D)omain (N)ame (S)erver

      * Protocolo de aplicação

      * **Função**: 
        * identificar endereços IP 
        * manter uma tabela com os endereços  dos cominhos de algumas rede

* **Interface de rede**

  * É um software e/ou hardware

  * **Função**: fazer a comunicação em uma rede de computadores

  * Interfaces de rede no Linux

    * **Localização**: diretório `/dev`

    * A maioria é criada dinamicamente pelos softwares quando são requisitadas

    * **Exemplo**: `eth0` - placa de rede Ethernet cabeada

  * Interface loopback

    * É um tipo especial de interface

    * **Função**: 

      * Permitir fazer conexões com você mesmo

      * Testar vários programas de rede sem interferir a rede local

    * Padrão do endereço IP: `127.0.0.1`

