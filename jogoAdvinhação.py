import random
from time import sleep

numeroPC = random.randint(1, 10)
numero = int(input("Tente descobrir um número de 1 até 10:\n"))

if numero == numeroPC:
    print("Parabéns! Você acertou.")
elif numero != numeroPC:
    sleep(2)
    numero2 = int(input("Segunda tentativa, digite um número de 1 até 10:\n"))
    if numero2 == numeroPC:
        print("Parabéns! Você acertou.")
    else:
        sleep(2)
        numero3 = int(input("Terceira tentativa, digite um número de 1 até 10:\n"))
        if numero3 == numeroPC:
            print("Parabéns! Você acertou.")
        else:
            sleep(2)
            print("Você perdeu. Tente novamente.")

# if numero == numeroPC:
#     print("Parabéns! Você acertou.")
# else:
#     print("Você errou.")
