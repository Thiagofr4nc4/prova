N, Q = map(int, input().split())
ListaAux = []
ListaAux2= []
Notas={}
for c in range(Q):
    NQi, IdQI = map(int, input().split())
    ListaAux.append(NQi)
    Notas[IdQI] = NQi
ListaAux.sort()
for c in range(N):
    v = ListaAux[c]
    ListaAux2.append(v)
C = int(input())
for c in range(C):
    NQi, IdQi = map(int, input().split())
    esq = 0
    dir = len(ListaAux2)-1
    while esq <= dir:
        meio = (esq + dir)//2
        if ListaAux2[meio] == NQi:
            break
        elif ListaAux2[meio] < NQi:
            esq = meio +1
        else:
            dir= meio -1
    if ListaAux[meio] == NQi:
        E = Notas[IdQi]
        E.sort()
        if E[0] == IdQi