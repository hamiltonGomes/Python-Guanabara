from datetime import date
from datetime import datetime

data = date.today()
dataHora = datetime.now() #utilizando datetime e now()

print(data.strftime(
    '%d/%m/%Y'))  # com "y" minúsculo ele imprime apenas os últimos dois números do ano. com "y" maiúsculo ele imprime o ano inteiro.

print(dataHora.strftime('%d/%m/%Y %H:%M')) #data e hora
