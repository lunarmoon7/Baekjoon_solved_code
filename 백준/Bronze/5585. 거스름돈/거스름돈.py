import sys

money = int(sys.stdin.readline())

money, ret = 1000 - money, 0
kinds = [500, 100, 50, 10, 5, 1]
for kind in kinds:
    if money >= kind:
        ret += money // kind
        money %= kind
        
print(ret)
        