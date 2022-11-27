import sys
import heapq

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n, k = map(int, input().split()) # 보석 개수, 가방 개수
jew = [] # 보석 무게, 가격 저장
bags = [] # 가방 무게 저장

for _ in range(n):
    heapq.heappush(jew, list(map(int, input().split())))

for _ in range(k):
    bags.append(input(int))
bags.sort() # 오름차순 정렬

total = 0
ret = []

for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(ret, -heapq.heappop(jew)[1])
    if ret:
        total -= heapq.heappop(ret)
    elif not jew:
        break
print(total)