N,M = map(int,input().split())
L = [0]*(2)
for i in range(N):
    S = list(input())
    z = S.count("0")
    o = S.count("1")
    if z % 2 == 0:
        L[0] += 1
    else:L[1] += 1
print(L[0]*L[1])