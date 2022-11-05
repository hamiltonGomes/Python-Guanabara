import random

aluno1 = str(input("Primeiro aluno:\n"))
aluno2 = str(input("Segundo aluno:\n"))
aluno3 = str(input("Terceiro aluno:\n"))
aluno4 = str(input("Quarto aluno:\n"))

listaAlunos = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(listaAlunos)

print(listaAlunos)