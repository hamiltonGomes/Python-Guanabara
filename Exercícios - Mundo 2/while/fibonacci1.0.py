print("------- FIBONACCI -------")

numero = int(input("Digite a quantidade de termos que deseja exibir na sequência: "))
termo1 = 0
termo2 = 1

if numero == 1:
    print({termo1})
else:
    print(f"{termo1} -> {termo2}", end='')

    contador = 3
    while contador <= numero:
        termo3 = termo1 + termo2
        print(f" -> {termo3}", end='')
        termo1 = termo2
        termo2 = termo3
        contador += 1
print(" -> Fim")
