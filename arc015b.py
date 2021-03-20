import sys
input = sys.stdin.readline
N = int(input())
mou,man,nat,net,tou,mah = 0,0,0,0,0,0
for i in range(N):
    a,b = map(float,input().split())
    if a >= 35: mou += 1
    elif a >= 30:man += 1
    elif a >= 25: nat += 1

    if b >= 25: net += 1
    if b < 0 and a >= 0: tou += 1
    if a < 0:mah += 1
print(mou,man,nat,net,tou,mah)