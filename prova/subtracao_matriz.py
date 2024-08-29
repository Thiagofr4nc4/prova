Matriz_Altura , Matriz_Largura = map(int,input().split())
Matriz_A = []
Matriz_B = []
Matriz_Resultante = []

for c in range (Matriz_Altura):
    J = list(map(int,input().split()))
    Matriz_A.append(J)

for c in range (Matriz_Altura):
    J = list(map(int,input().split()))
    Matriz_B.append(J)

for c in range (Matriz_Altura):
    M = 0
    for d in range (Matriz_Largura):
        Matriz_A[c][d] -= Matriz_B[c][d]
for c in range (Matriz_Altura):
    print(*Matriz_A[c], sep=' ')