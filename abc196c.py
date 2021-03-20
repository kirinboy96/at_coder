N = int(input())
i = "1"
ans = 0
while 1:
    if int(i+i) <= N:
        ans += 1
        i = str(int(i)+1)
    else:break
print(ans)