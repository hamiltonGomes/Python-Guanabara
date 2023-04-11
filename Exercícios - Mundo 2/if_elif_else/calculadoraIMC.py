print("Vamos descobrir seu índice de massa corporal!")


def imc(peso, altura):
    return peso / altura ** 2


print("Informe sua altura (em metros):")
altura1 = float(input())
print("Agora me diga quanto você pesa (kg):")
peso1 = float(input())
print("Seu IMC é de", round(imc(peso1, altura1), 2))

resultado = imc(peso1,altura1)

if resultado <= 18.5:
    print("Seu IMC é classificado como magreza.")
elif 18.5 <= resultado <= 24.9:
    print("Seu IMC é considerado normal.")
elif 25 <= resultado <= 29.9:
    print("Seu IMC é classificado como sobrepeso.")
elif 30 <= resultado <= 39.9:
    print("Seu IMC é classificado como obesidade.")
else:
    print("Seu IMC é classificado como obesidade grave.")