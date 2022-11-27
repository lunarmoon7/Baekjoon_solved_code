import sys

strs = sys.stdin.readline().split('-')

sums = 0
for i in range(1, len(strs)):
    sums += sum(map(int, strs[i].split('+')))

first_sums = sum(map(int, strs[0].split('+')))
print(first_sums - sums)