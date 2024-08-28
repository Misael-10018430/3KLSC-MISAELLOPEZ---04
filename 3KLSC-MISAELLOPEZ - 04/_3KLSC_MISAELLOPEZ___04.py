
matriz = [[0.0 for _ in range(5)] for _ in range(3)]


for i in range(3):
    for j in range(5):
        matriz[i][j] = float(input(f"Ingresa el valor en la posición [{i}][{j}]: "))


print("\nContenido de la matriz:")
for i in range(3):
    for j in range(5):
        print(matriz[i][j], end="  ")
    print("\n") 
