import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n, m = map(int, input().split()) # n : 기타줄 개수 , m : 기타줄 브랜드 개수
sets, nonSets = list(), list()
for _ in range(m):
    a, b = map(int, input().split())
    sets.append(a)
    nonSets.append(b)
sets.sort()
nonSets.sort()
total, mins = 0, float('inf')
for i in range(n // 6 + 2):
    j = n - 6 * i
    if j < 0:
        j = 0
    sums = sets[0] * i + nonSets[0] * j
    mins = min(mins, sums)
print(mins)