numero = int(input("digite um número:"))
print("dobro:", numero * 2)
triplo = numero * 3
print("triplo: {}".format(triplo))
raiz = numero ** (1 / 2)
print("a raiz quadrada de {} é {}".format(numero, raiz.__round__(2)))  # arredonda
print("a raiz quadrada de {} é {}".format(numero, raiz.__trunc__()))  ##exclui as casas decimais
