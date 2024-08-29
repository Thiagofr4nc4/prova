NumPlanetas = int(input())
Planetas_Visitados = list(map(int, input().split()))
Planetas_Visitados.sort()
Planetas_Analise = list(map(int, input().split()))

for c in Planetas_Analise:
    if c == 0:
        break
    esq = 0
    dire = len(Planetas_Visitados) -1
    while esq <= dire:
        meio = (esq + dire) // 2
        if (Planetas_Visitados[meio] == c):
            break
        elif (Planetas_Visitados[meio] > c):
            dire = meio - 1
        else:
            esq = meio + 1
    if Planetas_Visitados[meio] == c:
        print(meio)
    else:
        print('Nao foi visitado ainda.')
