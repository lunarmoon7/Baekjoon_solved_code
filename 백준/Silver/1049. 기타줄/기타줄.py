import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

n, m = map(int, input().split()) # n : 기타줄 개수 , m : 기타줄 브랜드 개수
sets, nonSets = float('inf'), float('inf') # sets : 6개 묶음 중 가장 값이 싼 것, nonSets : 낱개 중 가장 값이 싼 것

# 6개 묶음과 낱개에서 최소 가격만 사용하면 됨
# 나머지 가격들은 필요 없음
for _ in range(m):
    a, b = map(int, input().split())
    sets, nonSets = min(a, sets), min(b, nonSets) # 최소 가격 각각 저장
    
mins = float('inf') # mins : 적어도 n개를 교체하기 위해 필요한 최소 가격

# 예를 들어 예제 입력#4에서 17개 교체 시, 6개 묶음 2개와 낱개 5개를 사면 39원 필요, but 6개 묶음 3개를 사면 36원으로 더 저렴 
# 따라서 (n // 6 + 1) 까지 계산해봐야 함 
# (문제에서 적어도 n개 라고 명시되어있는 것도 이유 중 하나)
for i in range(n // 6 + 2): 
    j = n - 6 * i # 낱개 기타줄 개수
    if j < 0: # 예를 들어 예제 입력#4 일 때 6개 묶음이 3개라면 j = 17 - 6 * 3 = -1로 0보다 작게 됨 => 음수 기타줄 개수는 계산하지 않으므로 0으로 초기화 필요.
        j = 0
    sums = sets * i + nonSets * j # 총 비용의 합
    mins = min(mins, sums) # 가장 최소 비용을 저장
print(mins)