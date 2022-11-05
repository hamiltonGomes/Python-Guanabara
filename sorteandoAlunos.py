# import random
#
# aluno = random.randint(1, 4)
# print(aluno)

# match aluno:
#     case 1:
#         print("João irá apagar o quadro.")
#     case 2:
#         print("Marcos irá apagar o quadro.")
#     case 3:
#         print("José irá apagar o quadro.")
#     case 4:
#         print("Maria irá apagar o quadro.")

# if aluno == 1:
#     print("João irá apagar o quadro.")
# elif aluno ==2:
#     print("Marcos irá apagar o quadro.")
# elif aluno == 3:
#     print("José irá apagar o quadro.")
# else:
#     print("Maria irá apagar o quadro.")

# ----------------------------------------------------------------

import random

aluno1 = str(input("Primeiro aluno:\n"))
aluno2 = str(input("Segundo aluno:\n"))
aluno3 = str(input("Terceiro aluno:\n"))
aluno4 = str(input("Quarto aluno:\n"))
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
alunoEscolhido = random.choice(listaAlunos)
print(alunoEscolhido)
