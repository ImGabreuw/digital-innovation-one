# Entendendo o que é WSDL e XSD

### WSDL

> **WSDL** = (W)eb (S)ervices (D)escription (L)anguage

* Usando para descrever _Web Services_, funciona como um contrato do serviço

* A descrição é feita em um documento XML, onde é descrito o serviço (**Exemplo**: especificações de acesso / operações / métodos)

* **Representação do serviço com WSDL**

  * `www.soapclient.com/xml/soapresponder.wsdl`

  * `www.soapclient.com/xml/soapresponder?wsdl` (**mais comum**)

* [**SoapUI**](https://www.soapui.org/)

  > `Tools > SoapUI Open Source`

  * Criar um projeto SOAP

    * Barra de ferramentas: clique em **SOAP**

      * Project Name: automático

      * Initial WSDL: URI do serviço

    * Clique em **OK**

### XSD

> **XSD** = (X)ML (S)chema (D)efinition

* É um esquema no formato XML usado para definir a estrutura de dados que será validada no **XML**

* Funciona como ma documentação de como deve ser montado o _SOAP Message_ (**XML**) que será enviado através de _Web Services_