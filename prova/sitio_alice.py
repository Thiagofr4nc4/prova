A = int(input())
B = list(map(int, input().split()))
F = 0
for c in range(A):
    F = F + B[c]
    if (F == sum(B)/2):
        print(c + 1)