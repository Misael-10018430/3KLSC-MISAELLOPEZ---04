
matriz = [[0.0 for _ in range(5)] for _ in range(3)]

for fila in range(3):
    for columna in range(5):
        valor = float(input(f"Ingresa el valor en la posición [{fila}][{columna}]: "))
        matriz[fila][columna] = valor


for fila in range(3):
    for columna in range(5):
        print(matriz[fila][columna], end="  ")
    print("\n")
