N , M= map(int, input().split())
Mi = []
j=0
Egg = 0
x = 0
X=0
for c in range (N):
    Aux = list(map(int,input().split()))
    Mi.append(Aux)
while X != Mi[N-1][M - 1]:
    for i  in range (M):
        X = Mi[j][i]
        if X != 0:
            x += X
    j += 1
print(x)