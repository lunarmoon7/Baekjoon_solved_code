import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline()).strip()
n = input()
# 각 자릿수의 합이 3의 배수이고 0을 1개 이상 포함하는지
ret = ''.join(sorted(n)[::-1]) if '0' in n and sum(map(int, n)) % 3 == 0 else -1
print(ret)
