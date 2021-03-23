def solve(N, strs):
    ans = 0
    cntB = 0
    cntA = 0
    cntBA = 0
    for s in strs:
        ans += s.count("AB")
        if s[0] == "B" and s[-1] == "A":
            cntBA += 1
        elif s[0] == "B":
            cntB += 1
        elif s[-1] == "A":
            cntA += 1
    ans = ans + cntBA + min(cntA, cntB)
    if cntBA != 0 and cntA == 0 and cntB == 0:
        ans -= 1
    return ans


N = int(input())
strs = [input() for _ in range(N)]

print(solve(N, strs))
