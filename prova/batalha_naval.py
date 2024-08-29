H, L, Tiros = map(int,input().split())
Matriz = []
contador = 0
contador2 = 0
for C in range (H):
    Matriz.append(list(map(int,input().split())))
for X in range (H):
    for Y in range(L):
        if (Matriz[X][Y] == 1):
            contador += 1
for C in range (Tiros):
    X,Y = map(int,input().split())
    if Matriz[X][Y] == 1:
        Matriz[X][Y] = 0
        contador2 += 1
if contador2 >= contador/2:
    print('Bira')
else:
    print('Vidal')