from Extras import datetime

ano = int(input("Insira o ano que deseja descobrir se é bissexto:\n"))

if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano de {} é bissexto.".format(ano))
else:
    print("O ano de {} não é bissexto.".format(ano))

# 4 8 2 6 0