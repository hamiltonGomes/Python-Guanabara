print("-" * 10, "SEQUÊNCIA DE FIBONACCI", "-" * 10)

N = int(input("Quantos termos deseja mostrar?\n"))
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
