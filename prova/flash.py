N, M = map(int, input().split())
L = list(map(int, input().split()))
L_filtrado = [l for l in L if l != 0]
resultado = L_filtrado[-M:]
print(" ".join(map(str, resultado)))
