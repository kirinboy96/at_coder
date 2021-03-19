A,B,W = map(int,input().split())
W *= 1000
l,r = 1<<30,0
for i in range(1,W+1):
    if A*i <= W <= B*i:
        l = min(i,l)
        r = max(i,r)
if l == 1 << 30:
    print("UNSATISFIABLE")
else:
    print(l,r)
