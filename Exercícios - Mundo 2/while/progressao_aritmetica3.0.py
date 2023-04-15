from time import sleep

print("-" * 20, "GERADOR DE PA 3.0", "-" * 20)

primeiro_termo = int(input("Digite o primeiro termo da progressão aritmética: \n"))
razao = int(input("Agora digite a razão: \n"))
while razao == 0:
    razao = int(input("A razão não pode ser 0. Por favor, digite outro valor: \n"))
numeroTermos = 10
contador = 1
termos = []

while True:
    while contador <= numeroTermos:
        termo = primeiro_termo + (contador - 1) * razao
        contador += 1
        termos.append(termo)
        if contador == numeroTermos:
            print(f"A progressão aritmética é: {', '.join(map(str, termos))}.", end=" ")
            sleep(2)
            mais = int(input("\nQuantos termos deseja adicionar a progressão?\n"))
            if mais == 0:
                print("Obrigado por utilizar meu programa.")
                print(f"A PA teve {numeroTermos} termos.")
                break
            else:
                numeroTermos += mais
