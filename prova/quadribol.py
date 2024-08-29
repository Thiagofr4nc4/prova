Participantes = int(input())
A = sorted(list(map(int, input().split())))
print(*A[:8],sep=' ')