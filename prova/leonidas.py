Matriz_Inicial = []
ValorBugante = int(input())
M = 0
for j in range (10):
    Matriz_Inicial.append(list(map(int,input().split())))
for j in range (10):
    if M == 'sim':
        break
    for c in range (10):
        if ValorBugante == Matriz_Inicial[j][c]:
            M = 'sim'
            break
        else:
            M = 'nao'
print(M)