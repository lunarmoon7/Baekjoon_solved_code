n = int(input())
num_list = list(map(int, input().split())) # 입력 : 1 2 3 => [1, 2, 3] 저장
num_list.sort()

total, prev = 0, 0
for i in num_list:
    cur = i
    sums = prev + cur
    total += sums
    prev = sums
print(total)
    
    