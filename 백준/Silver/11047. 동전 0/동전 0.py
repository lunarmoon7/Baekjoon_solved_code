n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

total = 0
for coin in reversed(coins):
    total += k // coin
    k = k % coin
    
print(total)