total = 0

for i in range(1, 500, 2):
    if i % 3 == 0:
        total += i
print(f'A soma de todos os números ímpares e múltiplo de 3 é {total}')
