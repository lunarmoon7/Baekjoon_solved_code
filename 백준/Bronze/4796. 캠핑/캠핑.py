import sys

def input(type=str): # 입력 함수 재정의
    return type(sys.stdin.readline())
def input_s(type=str):
    return type(sys.stdin.readline()).strip()

caseNum = 1
while 1:
    l, p, v = map(int, input_s().split())
    if l == 0 and p == 0 and v == 0:
        break
    
    ret = (v // p) * l
    ret += min((v % p), l)
    print("Case %d: %d" %(caseNum, ret))
    caseNum += 1
    # a, b = v // p, v % p
    # if l < b:
    #     b = l
    # print("Case %d: %d" %(caseNum, a * l + b))