"""
The challenge is to create a two Mario-style staircase,
similar to the ones found in the final stages of the Mario Bros. game.
"""

validate = True

while validate:
    stair_height = int(input("Digite um número de 1 a 8:"))
    if stair_height >= 9 or stair_height <= 0:
        validate = True
    else:
        validate = False

for i in range(0, stair_height + 1):
    print(" " * (stair_height - i) + "#" * i + " " + "#" * i + " " * (stair_height - i))
