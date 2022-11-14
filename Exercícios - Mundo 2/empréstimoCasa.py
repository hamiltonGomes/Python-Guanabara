valorCasa = int(input("Qual o valor da casa?\n"))
salario = int(input("Qual o valor do seu salário?\n"))
anos = float(input("Quantos anos pretende quitar o empréstimo?\n"))

mensais = 12 * anos
prestacaoMensal = valorCasa / mensais

if prestacaoMensal > (salario * 0.3):
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado com parcelas mensais de R$ {:.2f} durante {} meses.".format(prestacaoMensal, mensais))
