# Criando nosso primeiro container

### Comandos

* **Verificar os recursos gastos em cada _container_**: `$ docker stats`

* **Criar um _container_**: `docker run <imagem>`

* **Criar um _container_ como nome customizado**: `docker run --name <nome> <imagem>`

* **Criar um _container_ com binding de portas**: `$ docker run -p <porta máquina local>:<porta container>`

* **Remover um _container_**: `$ docker container rm <nome/ID>`

* **Forçar a remoção de um _container_**: `$ docker rm -f <nome/ID>`

* **Remover uma imagem**: `$ docker rmi <nome/ID>`

* **Listar as imagens salvas na máquina local**: `$ docker images` ou `$ docker image ls`

* **Listar os _containers_ em execução**: `$ docker container ls` ou `$ docker ps`