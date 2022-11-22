T = int(input("Digite o valor total de unidades de sapatos.\n"))
dic = {'R': [],
       'L': []}
pares = 0

for x in range(T):
    sapato = input(
        "Informe o tamanho do sapato e qual o seu lado (\"R\" para direito ou \"L\" para esquerdo), separando os valores com espaço.\n").split()
    num = int(sapato[0])
    lado = sapato[1]

    if lado == 'R':
        ladoOposto = "L"
    else:
        ladoOposto = 'R'
    if num in dic[ladoOposto]:
        dic[ladoOposto].remove(num)
        pares += 1
    else:
        dic[lado].append(num)

print("Foram formados {} pares de sapatos.".format(pares))
