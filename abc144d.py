import math
a,b,x = map(int, input().split())
v = a*a*b
if 2*x <= v:
  ans = math.degrees(math.atan(a*b*b/(2*x)))
  print(ans)
else:
  ans = math.degrees(math.atan((2*a*a*b-2*x)/a**3))
  print(ans)