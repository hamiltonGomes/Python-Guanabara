cidade = input("Diga qual o nome de uma cidade:\n")
santo = cidade.strip().lower().find("santo")

if santo == 0:
    print("O nome da sua cidade começa com \"Santo\"!")
else:
    print("O nome da sua cidade não começa com \"Santo\"!")
