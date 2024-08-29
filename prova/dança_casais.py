Num = int(input())
Homens = list(map(int,input().split()))
Homens.sort(reverse = True)
Mulheres = sorted(list(map(int,input().split())))
for i in range (Num):
    print(Homens[i],Mulheres[i])