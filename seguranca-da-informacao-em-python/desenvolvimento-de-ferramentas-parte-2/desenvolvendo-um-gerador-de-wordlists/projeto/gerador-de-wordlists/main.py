import itertools
import string
import random

chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.;:/?ç"
rnd = random.SystemRandom()
word = "".join(rnd.choice(chars) for i in range(16))
resultado = itertools.permutations(word, len(word))

for i in resultado:
    print("".join(i))
