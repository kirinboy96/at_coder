N = input()

if N.count(".") == 0:
    print(N)
else:
    pl = N.index(".")
    print(N[:pl])