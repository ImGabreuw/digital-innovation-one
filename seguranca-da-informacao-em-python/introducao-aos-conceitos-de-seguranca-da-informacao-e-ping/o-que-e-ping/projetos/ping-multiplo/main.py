import os
import time

with open("hosts.txt") as file:
    dump = file.read()

    for ip in dump.split("\n"):
        print("Verificando o IP: ", ip)

        print("-" * 60)
        os.system("ping -c 2 {}".format(ip))
        print("-" * 60)

        time.sleep(5)
