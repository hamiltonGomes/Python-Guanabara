lista = []
resposta = "S"

while resposta in "Ss":
    termo = int(input("Adicione valores na lista: \n").strip())
    lista.append(termo)
    resposta = str(input("Deseja continuar? (S/N)\n")).strip()[0]
    while resposta not in "NnSs":
        resposta = str(input("Resposta inválida. Digite uma opção válida (S/N): \n")).strip()[0]

print(set(', '.join(map(str, lista))))
