import random

random.seed(2) #para emitir uma aleatoriedade o python busca criar uma nova seed a cada milisegundo, no entanto, é possível definir uma seed antecipadamente.

numeroSorteado = random.randrange(1, 11)
print(f'o número sorteado é {numeroSorteado}')
