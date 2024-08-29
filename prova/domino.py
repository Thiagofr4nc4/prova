matriz = []
for _ in range(7):
    linha = list(map(int, input().split()))
    matriz.append(linha)
contador_pecas = 0
for i in range(7):
    for j in range(7):
        if matriz[i][j] == 1 and i <= j:
            contador_pecas += 1
print(contador_pecas)
