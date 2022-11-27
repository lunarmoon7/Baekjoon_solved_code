import sys

n = int(sys.stdin.readline())
ropes = list(int(sys.stdin.readline()) for _ in range(n))

ropes.sort(reverse=True)
maxs = ropes[0] * 1
for i in range(1, n):
    maxs = max(maxs, ropes[i] * (i + 1))
print(maxs)