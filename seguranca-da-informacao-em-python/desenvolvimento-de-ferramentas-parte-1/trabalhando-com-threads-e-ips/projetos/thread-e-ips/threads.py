import time
from threading import Thread


def carro(velocidade, piloto):
    trajeto = 0

    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print(f"Piloto {piloto} - Km: {trajeto} \n")


thread_carro1 = Thread(target=carro, args=[7, "Bruno"])
thread_carro2 = Thread(target=carro, args=[10, "Python"])

thread_carro1.start()
thread_carro2.start()
