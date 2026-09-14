import random
import string
def gerarNumero (x, y):
    return random.randint(x, y)
alfabeto = list(string.ascii_lowercase)
letra = alfabeto[random.randint(0,25)]
senha = letra + str(gerarNumero(0,9)) + str(gerarNumero(0,9))
print(senha)