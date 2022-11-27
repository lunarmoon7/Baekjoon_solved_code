import sys

# input
n = int(input())
times = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

times.sort(key=lambda end: (end[1], end[0]))

prevEnd, cnt = -1, 0
for start, end in times:
    if start >= prevEnd:
        prevEnd = end
        cnt += 1
print(cnt)