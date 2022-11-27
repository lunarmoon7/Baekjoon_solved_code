import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())

s = input(int)

sum, num = 0, 0
while sum <= s:
    num += 1
    sum += num
    
print(num if sum == s else num - 1)