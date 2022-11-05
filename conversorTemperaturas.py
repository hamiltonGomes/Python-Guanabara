celsius = int(input("Digite o valor da temperatura em Celsius:\n"))
temperatura = int(input("Digite qual escala termométrica deseja converter:\n1 - Kelvin\n2 - Fahrenheit\n"))
if temperatura == 1:
    constKelvin = 273.15
    kelvin = celsius + constKelvin
    print("O valor em Kelvin é {} K.".format(kelvin))
elif temperatura == 2:
    fahrenheit = celsius * (9 / 5) + 32
    print("O valor em Fahrenheit é {} ºF.".format(fahrenheit))
else:
    print("Valor inválido.")
