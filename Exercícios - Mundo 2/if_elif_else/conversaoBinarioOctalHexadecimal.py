print("Conversor Binário/Octal/Hexadecimal!")

numero = int(input("Qual número deseja converter?\n"))
opcao = int(input("Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n4 - Cancelar\n"))

if opcao == 1:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, bin(numero)))
elif opcao == 2:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, oct(numero)))
elif opcao == 3:
    print("{} convertido para BINÁRIO é igual a {}".format(numero, hex(numero)))
elif opcao == 4:
    print("Programa finalizado.")
