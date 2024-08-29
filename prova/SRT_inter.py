A = int(input())
B= {}
E=[]
for c in range(A):
    X , Y = map(int, input().split())
    E.append(Y)
    Y=str(Y)
    B[Y] = X
E.sort(reverse=True)
for X in range(A):
    J = E[X]
    print(B[str(J)], J)