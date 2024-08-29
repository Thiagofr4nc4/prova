Matriz_Altura , Matriz_Largura = map(int,input().split())
MatrizDeBugs = []
cont1 = 0
cont2 = 0
for c in range (Matriz_Altura):
    J = list(map(int, input().split()))
    MatrizDeBugs.append(J)
Balas = int(input())

for c in range (Matriz_Altura):
    for d in range (Matriz_Largura):
        if (MatrizDeBugs[c][d] == 1):
            cont1 += 1

for c in range(Balas):
    A , B = map(int, input().split())
    if (MatrizDeBugs[A - 1][B - 1] == 1):
        cont2 += 1
        MatrizDeBugs[A - 1][B - 1] = 0
if cont1 == cont2:
    print('HASTA LA VISTA BABY')
else:
    print('ILL BE BACK')