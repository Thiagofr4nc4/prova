Novidade! Atalhos do teclado … 
Os atalhos de teclado do Drive foram atualizados para oferecer navegação por letras iniciais

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p +1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for k in range(inicio, fim):
        if lista[k] <= pivot:
            lista[k], lista[i] = lista[i], lista[k]
            i=+1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

N, M = map(int, input().split())
Matriz=[]
for c in range(M):
    a = list(map(int, input().split()))
    quicksort(a)
    Matriz.append(a)
H= int(input())
Q= list(map(int,input().split()))
for j in Q:
    contador=0
    for c in range(N):
        for d in range(M):
            if Matriz[c][d] <= j:
                contador+=1
            else:
                break
    print(contador)
