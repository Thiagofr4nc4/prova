quantia_barcos = int(input())
lista = []
for i in range(quantia_barcos):
    barco = int(input())
    lista.append(barco)
lista.sort([-1])
print(lista)
