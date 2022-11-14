# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

x = input("Digite algo\n")
print(type(x))
print("Ele é só tem espaço?", x.isspace())
print("Ele é numérico?", x.isnumeric())
print("Ele é alfabético?", x.isalpha())
print("Ele é alfanumérico?", x.isalnum())
print("Ele está em maiúsculo?", x.isupper())
print("Ele está em minúsculo?", x.islower())
print("Ele está capitalizada?", x.istitle())

