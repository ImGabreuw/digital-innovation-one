# Limites

### Limitar o uso de memória de um _container_

* **Sintaxe**: `$ docker run -d --memory <quantidade em megabyte> <imagem>`

* **Exemplo**: `$ docker run -d --memory 30m busybox sleep 3600

### Limitar o uso de CPU de um _container_

* **Sintaxe**: `$ docker run -d --cpus="<quantidade>" <imagem>`

* **Exemplo**: `$ docker run -d --cpus="1.5" busybox sleep 3600