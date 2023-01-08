from functools import reduce
import math
def isMod(arr, gcd):
    for num in arr:
        if num % gcd == 0: return True
    return False
def solution(arrayA, arrayB):
    answer = 0
    n = len(arrayA)
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    for i in range(1, n):
        gcd_a = math.gcd(gcd_a, arrayA[i])
        gcd_b = math.gcd(gcd_b, arrayB[i])
        
    if gcd_a != 1:
        if not isMod(arrayB, gcd_a):
            answer = gcd_a
    if gcd_b != 1:
        if not isMod(arrayA, gcd_b):
            answer = max(answer, gcd_b)
    # if gcd_a == 1:
    #     if isMod(arrayA, gcd_b): return 0
    #     return gcd_b
    # elif gcd_b == 1:
    #     if isMod(arrayB, gcd_a): return 0
    #     return gcd_a
    # else:
    #     isMod_a = isMod(arrayB, gcd_a)
    #     isMod_b = isMod(arrayA, gcd_b)
    #     if isMod_a and isMod_b: return 0
    #     if isMod_a:
    #         if not isMod_b: return gcd_b
    #     if isMod_b:
    #         if not isMod_a: return gcd_a
    #     if not isMod_a and not isMod_b: return max(gcd_a, gcd_b)
        
    return answer