N = int(input())
L = list(map(int,input().split()))
for i in range(N-1):
    if L[i] < L[i+1]:
        L[i+1] -= 1
    if L[i] > L[i+1]:
        print("No")
        break
else:print("Yes")
