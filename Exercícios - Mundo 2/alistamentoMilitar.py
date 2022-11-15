print("ALISTAMENTO MILITAR")
idade = int(input("Qual sua idade?\n"))

if idade == 18:
    print("É hora de fazer o alistamento militar.")
elif idade > 18:
    anosExcedidos = idade - 18
    print("Já passou {} anos da idade de realizar o alistamento militar obrigatório.".format(anosExcedidos))
elif idade < 18:
    anosFaltam = 18 - idade
    print("Faltam {} anos para você se alistar.".format(anosFaltam))
