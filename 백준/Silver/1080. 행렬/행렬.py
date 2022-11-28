import sys
import heapq


def input(type=str):  # 입력 함수 재정의
    return type(sys.stdin.readline())


def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n, m = map(int, input().split())
a = [list(map(int, input_s())) for _ in range(n)]
b = [list(map(int, input_s())) for _ in range(n)]
cnt = 0

def flip(x, y):
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            a[i][j] = 1 - a[i][j]

for i in range(n - 2):
    for j in range(m - 2):
        if a[i][j] != b[i][j]:
            flip(i, j)
            cnt += 1
if a != b:
    print(-1)
else:
    print(cnt)