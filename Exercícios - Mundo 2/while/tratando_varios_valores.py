valores = []
while True:
    valor = int(input("Digite qualquer valor: "))
    if valor == 999:
        break
    else:
        valores.append(valor)

print(f"\nOs total de números digitados foi: {len(valores)}.")
print(f"Os valores digitados foram: {', '.join(map(str, valores))}.")
print(f"A soma desses valores é: {sum(valores)}.")
