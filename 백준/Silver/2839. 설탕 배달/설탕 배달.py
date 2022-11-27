n = int(input())
totalCnt = 0

while True:
    if n % 5 == 0:
        totalCnt += n // 5
        print(totalCnt)
        break
    n -= 3
    totalCnt += 1
    if n < 0:
        print(-1)
        break