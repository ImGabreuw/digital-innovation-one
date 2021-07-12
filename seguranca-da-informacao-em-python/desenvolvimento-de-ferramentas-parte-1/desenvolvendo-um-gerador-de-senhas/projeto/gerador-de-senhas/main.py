import random
import string

tamanho_da_senha = int(input("Informe o tamanho da senha: "))

# chars = "a-z" + "A-Z" + "0-9" + "!@#$%&*()-=+,.;:/?"
chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;:/?ç"
rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(tamanho_da_senha)))
