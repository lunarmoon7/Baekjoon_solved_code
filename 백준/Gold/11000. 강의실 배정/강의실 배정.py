import sys
import heapq


def input(type=str):  # 입력 함수 재정의
    return type(sys.stdin.readline())


def input_s(type=str):
    return type(sys.stdin.readline()).strip()


n = input(int)
times = []
# times = [list(map(int, input().split())) for _ in range(n)]
for _ in range(n):
    item = list(map(int, input().split()))
    times.append(item)
times.sort()

heap = []
heapq.heappush(heap, times[0][1])
for i in range(1, n):
    if heap[0] > times[i][0]:
        heapq.heappush(heap, times[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, times[i][1])
print(len(heap))