# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

frase = str(input("Digite sua frase: \n")).strip()  # retirei os espaços entre as palavras
palavras = frase.split()  # dividi a frase de cima por palavras e coloquei na lista "palavras"
junto = ''.join(palavras)  # juntei todas as palavras da lista nessa String
inverso = ''

for letra in range(len(junto) - 1, -1, -1): # esse for inicia na última letra da string criada na variável "junto", termina no -1 e retrocede com o -1 no passo
    inverso += junto[letra]  # aqui estou percorrendo e acrescentando cada letra da string "junto" a varíavel "inverso"

print(inverso)

if inverso == junto:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")
