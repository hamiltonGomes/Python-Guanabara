palavra = str(input("Digite um string:\n"))


def findLen(palavra):
    i = 0
    for x in palavra:
        i += 1
    return i


print(findLen(palavra))
