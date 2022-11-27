import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
n = input(int)
roads = list(map(int, input().split()))
liters = list(map(int, input().split()))


prev = 0
cur = prev + 1
ret = roads[0] * liters[0]

# ret = 0
while cur < n - 1:
    if liters[prev] < liters[cur]:
        ret += liters[prev] * roads[cur]
    else:
        ret += liters[cur] * roads[cur]
        prev = cur
    cur += 1
print(ret)

