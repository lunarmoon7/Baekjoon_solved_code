import sys

# input
n = int(input())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()

sums = 0
for i in range(len(a)):
    mins = a[i]
    maxs = b.pop(b.index(max(b)))
    sums += mins * maxs
print(sums)

