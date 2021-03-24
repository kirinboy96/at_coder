A,G,B = map(int,input().split())
K = int(input())
if A < G < B:
    print("Yes")
    exit(0)
for i in range(K):
    if A >= G:
        G *= 2
    elif G >= B:
        B *= 2
if A < G < B:
    print("Yes")
    exit(0)
print("No")