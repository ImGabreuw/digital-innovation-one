# Principais Comandos

* **Criar um _container_**: `$ docker run <imagem>`

* **Criar um _container_ com nome personalizado**: `$ docker run --name <nome> <imagem>`

* **Criar um _container_ com binding de portas**: `$ docker run <imagem> -p <porta máquina local>:<porta container>`

* **Visualizar informações do Docker**: `$ docker info`

* **Iniciar um _container_**: `$ docker start <nome/ID>`

* **Parar um _container_**: `$ docker stop <nome/ID>`

* **Ver os logs de um _container_**: `$ docker logs <nome/ID>`

* **Baixar uma imagem de um repositório do _Docker Hub_**: `$ docker pull <imagem>`

* **Fazer um commit**: `$ docker commit --author="<autor>" --message="<mensagem>" <container> <imagem>`

* **Criar uma tag para uma imagem**: `$ docker tag <imagem base> <usuário no Docker Hub>/<nome da imagem>:<versão>`

* **Buscar por uma imagem específica no Docker Hub**: `$ docker search <imagem>`

* **Exportar um arquivo do sistema de um _container_ como arquivo compactado**: `$ docker export <container> > <nome do arquivo compactado>`

* **Importar um arquivo do sistema de um container para outro**: `$ docker import - <nome>`