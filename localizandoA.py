frase = input("Digite o que desejar:")
print("Quantas vezes aparece a letra \"a\":", frase.lower().count("a"))
print("A primeira aparição da letra \"a\" é na posição:", frase.lower().find("a")+1)
print("A última aparição da letra \"a\" é na posição:", frase.lower().rfind("a")+1)

