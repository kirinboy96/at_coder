N,M,Q = map(int,input().split())
WV = []
for i in range(N):
    a,b = map(int,input().split())
    # 大きさ
    WV.append([a,b])
    # 価値
WV.sort()
X = list(map(int,input().split()))
for i in range(Q):
    l,r = map(int,input().split())
    l -= 1
    tmp = X[:l] + X[r:]
    tmp.sort()
    ans = 0
    visited = [False] * N
    for j in range(len(tmp)):
        ans1 = 0
        place = -1
        for k in range(N):
            if tmp[j] < WV[k][0] or visited[k] != False:
                continue
            if WV[k][1] > ans1:
                ans1 = WV[k][1]
                place = k
        ans += ans1
        if place >= 0:
            visited[place] = True
    print(ans)




