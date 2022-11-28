import sys
import heapq

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n, l = map(int, input().split())
pos = list(map(int, input().split()))
pos.sort()

start, cnt = pos[0], 1

for loc in pos[1:]:
    if loc in range(start, start + l):
        continue
    else:
        start = loc
        cnt += 1
print(cnt)
        





