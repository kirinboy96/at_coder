N,K = map(int,input().split())
hands = list(map(int,input().split()))
T = list(input().replace('r','2').replace('s','0').replace('p','1'))
ans = 0
for i in range(N):
    if i < K:
        ans += hands[int(T[i])]
    else:
        if T[i] == T[i-K]:
            T[i] = "X"
        else:
            ans += hands[int(T[i])]
print(ans)