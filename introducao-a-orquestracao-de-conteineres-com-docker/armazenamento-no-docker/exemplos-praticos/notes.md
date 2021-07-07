# Exemplos práticos

### _mount_ do tipo **volume**

* **Criar o volume** 

  * **Sintaxe**: `$ docker volume create <nome>`

  * **Exemplo**: `$ docker volume create meuPrimeiroVolume`

* **Listar os volumes**: `$ docker volume ls`

* **Exibir informações detalhadas de um volume**

  * **Sintaxe**: `$ docker volume inspect <nome>`

  * **Exemplo**: `$ docker volume inspect meuPrimeiroVolume`

  * **Saída** (formato JSON)

    ```json
    [
      {
        "CreatedAt": "2021-07-07T12:17:29-03:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/meuPrimeiroVolume/_data",
        "Name": "meuPrimeiroVolume",
        "Options": {},
        "Scope": "local"
      }
    ]
    ```

* **Criar um container especificando um _mount_ do tipo volume**

  * **Sintaxe**: 

    * `$ docker run -d -p 80:80 --name <nome container> --mount source=<nome volume host>,target=<nome volume container> <imagem>`

    * `$ docker run -d -p 80:80 --name <nome container> -v <caminho volume host>:<caminho volume container> <imagem>`

  * **Exemplo**: 
    
    * `$ docker run -d -p 80:80 --name container-volume --mount source=meuPrimeiroVolume,target=/usr/share/nginx nginx`

    * `$ docker run -d -p 80:80 --name container-volume -v /var/lib/docker/volumes/meuPrimeiroVolume/_data/html:/usr/share/nginx nginx`

### _mount_ do tipo **tmpfs**

* **Criar um container especificando um mount do tipo tmpfs**

  * **Sintaxe**: `$ docker run -d --name <nome> --mount type=tmpfs,destination=<caminho container>,tmpfs-size=<espaço em byte> <imagem>`

  * **Exemplo**: `$ docker run -d --name container-tmpfs --mount type=tmpfs,destination=/cache,tmpfs-size=1000000 busybox sleep 3600`