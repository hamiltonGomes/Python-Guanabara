salario = float(input("Digite seu salário:\n"))

if salario > 1250:
    salario10 = salario * 1.10
    print("Seu novo salário é R$ {:.2f}".format(salario10))
else:
    salario15 = salario * 1.15
    print("Seu novo salário é R$ {:.2f}".format(salario15))
