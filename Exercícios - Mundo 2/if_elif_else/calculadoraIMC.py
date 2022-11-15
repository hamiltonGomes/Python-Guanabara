print("Vamos descobrir seu índice de massa corporal!")


def imc(peso, altura):
    return peso / altura ** 2


print("Informe sua altura (em metros):")
altura1 = float(input())
print("Agora me diga quanto você pesa (kg):")
peso1 = float(input())
print("Seu IMC é de", round(imc(peso1, altura1), 2))

if imc(peso1, altura1) <= 18.5:
    print("Seu IMC é classificado como magreza.")
elif 18.5 <= imc(peso1, altura1) <= 24.9:
    print("Seu IMC é considerado normal.")
elif 25 <= imc(peso1, altura1) <= 29.9:
    print("Seu IMC é classificado como sobrepeso.")
elif 30 <= imc(peso1, altura1) <= 39.9:
    print("Seu IMC é classificado como obesidade.")
else:
    print("Seu IMC é classificado como obesidade grave.")