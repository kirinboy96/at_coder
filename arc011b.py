N = int(input())
L = list(map(str,input().lower().split()))
A = []
D = ['z','r','b','c','d','w','t','j','f','q','l','v','s','x','p','m','h','k','n','g']
for i in range(N):
    S = []
    for j in range(len(L[i])):
        if L[i][j] in ("a",'e','i','o','u','y','.',','):
            continue
        S.append(str(D.index(L[i][j])//2))
    if len(S) != 0:
        A.append("".join(S))
print(*A)