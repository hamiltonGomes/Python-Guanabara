print("-"*20)
print("GERADOR DE PA 2.0")
print("-"*20)

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: \n"))
razao = int(input("Agora digite a razão: \n"))
contador = 1
termos = []

while contador < 11:
    termo = primeiro_termo + (contador - 1) * razao
    contador += 1
    termos.append(termo)

print(f"A progressão aritmética é: {', '.join(map(str, termos))}.", end=" ")
