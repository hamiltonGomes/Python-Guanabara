numero1 = int(input("Escreva o primeiro valor:\n"))
numero2 = int(input("Escreva o segundo valor:\n"))

if numero1 > numero2:
    print("O número 1 é maior que o número 2.")
elif numero2 > numero1:
    print("O número 2 é maior que o número 1.")
else:
    print("Não existe valor maior, ambos são iguais.")