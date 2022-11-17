print("-" * 10, "SEQUÊNCIA DE FIBONACCI", "-" * 10)

N = int(input("Quantos termos deseja mostrar na sequência? (Minímo de 1 e máximo de 47.)\n"))

while 0 > N or N >= 47:
    N = int(input("Digite um valor válido entre 1 e 47.\n"))

if N == 0:
    print("O número digitado impossibilita a criação de uma sequência de Fibonacci. Programa finalizado.")
elif N == 1:
    print(0)
else:
    t1 = 0
    t2 = 1
    print("{} {}".format(t1, t2), end='')

    cont = 3
    while cont <= N:
        t3 = t1 + t2
        print(" {}".format(t3), end='')
        t1 = t2
        t2 = t3
        cont += 1
