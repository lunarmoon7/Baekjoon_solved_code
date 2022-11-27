import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

s = input().strip()

split_one = s.replace('1', ' ').split()
split_zero = s.replace('0', ' ').split()

one_len = len(split_one)
zero_len = len(split_zero)

print(one_len if zero_len > one_len else zero_len)