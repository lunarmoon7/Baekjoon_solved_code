import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

s = list(map(int, input_s().split()))
a, b, cnt = s[0], s[1], 1

while a != b:
    if b < a:
        cnt = -1
        break
    if b % 10 != 1 and b % 2 != 0:
        cnt = -1
        break
    if b % 10 == 1:
        b //= 10
    else:
        b //= 2
    cnt += 1
print(cnt)