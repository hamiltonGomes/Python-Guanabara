from datetime import date

data = date.today()

anoNascimento = int(input("Em que ano você nasceu?"))
idade = data.year - anoNascimento

if 0 < idade < 9:
    print("Categoria MIRIM.")
elif 9 < idade <= 14:
    print("Categoria INFANTIL.")
elif 14 < idade <= 19:
    print("Categoria JUNIOR.")
elif 19 < idade <= 20:
    print("Categoria SÊNIOR.")
elif idade > 20:
    print("Categoria MASTER.")
else:
    print("Idade inválida.")
