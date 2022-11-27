import sys

t = int(sys.stdin.readline())

300, 60, 10

a = t // 300
t %= 300
b = t // 60
t %= 60
c = t // 10
t %= 10

if t != 0:
    print(-1)
else:
    print(a, b, c)
