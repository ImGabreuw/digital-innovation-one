# Exemplos Práticos 

### Comandos

* **Visualizar os tipos de rede de cada _container_**: `$ docker network ls`

* **Criar um rede**: 

  * **Sintaxe**: `$ docker network create -d <tipo da rede> <nome da rede>`

  * **Exemplo**: `$ docker network create -d bridge petsBridge`

* **Criar um _container_ definindo uma rede**
  
  * **Sintaxe**: `$ docker run -d --net <nome da rede> --name <container> <imagem>`

  * **Exemplo**: `$ docker run -d --net petsBridge --name db consul`

* **Criar um _container_ com variáveis de ambientes**

  * **Sintaxe**: `$ docker run --env "<chave>=<valor>" <imagem>`

  * **Exemplo**: `$ docker run -d --env "DB=db" --net petsBridge --name web -p 8000:5000 chrch/docker-pets:1.0`