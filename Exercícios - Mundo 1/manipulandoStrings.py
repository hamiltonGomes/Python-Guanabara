nome = "amilton amilton amilton amilton amilton"
print(nome.count("a", 0, 4))  # conta os termos em um determinado intervalo ou não
print(nome.find(
    'b'))  # vai informar em que momento ele encontrou o termo na string. quando ele retornar -1 quer dizer que ele não encontrou.
print(nome.replace("amilton", "gomes"))  # troca os termos
print(nome.lower())  # coloca os termos em minúsculo
print(nome.upper())  # coloca os termos em maiúsculo
print(nome.capitalize())  # coloca o primeiro termos em maiúsculo
print(nome.title())  # coloca a primeira letra de cada palavra em maiúsculo
print(nome.strip())  # remove todos os espaços inúteis (geralmente no início e no final)
print(nome.rstrip())  # remove todos os espaços inúteis (geralmente da direita)
print(nome.lstrip())  # remove todos os espaços inúteis (geralmente da esquerda)
print(nome.split())  # realiza divisão das strings em uma lista
print('-'.join(nome))  # realiza a junção das strings em uma lista
print(' '.join(nome))  # realiza a junção das strings em uma lista
print(len(nome.replace(" ", "x")))
print(nome.replace(" ", "x").count("x"))
