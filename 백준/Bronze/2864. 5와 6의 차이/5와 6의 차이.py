import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

a, b = input().split()
minA, minB = int(a.replace('6', '5')), int(b.replace('6', '5'))
maxA, maxB = int(a.replace('5', '6')), int(b.replace('5', '6'))

minSum = minA + minB
maxSum = maxA + maxB

print(minSum, maxSum)