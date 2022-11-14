nome = input("Escreva seu nome completo:\n").strip()
nomeSeparado = nome.split()
print(nomeSeparado[2])
print(len(nomeSeparado))

print("Nome completo: {}".format(nome))
print("Primeiro nome: {}".format(nomeSeparado[0]))
print("Último nome: {}".format(nomeSeparado[len(nomeSeparado)-1])) #pq o len conta o total de termos, mas pra referenciar a posição do último nome é necessário subtrair 1
