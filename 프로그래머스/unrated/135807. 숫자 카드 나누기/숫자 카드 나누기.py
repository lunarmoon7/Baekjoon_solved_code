from functools import reduce
import math
# def lcm(a, b):
#     return (a * b) // math.gcd(a, b)
def solution(arrayA, arrayB):
    answer = 0
    isMod_a, isMod_b = False, False
    gcd_a, gcd_b = arrayA[0], arrayB[0]
    for i in range(1, len(arrayA)):
        gcd_a = math.gcd(gcd_a, arrayA[i])
        gcd_b = math.gcd(gcd_b, arrayB[i])
    # lcm_a = reduce(lambda x, y: x * y, arrayA) // gcd_a
    # lcm_b = reduce(lambda x, y: x * y, arrayB) // gcd_b
    if gcd_a == 1:
        for num in arrayA:
            if num % gcd_b == 0:
                return 0
        return gcd_b
    elif gcd_b == 1:
        for num in arrayB:
            if num % gcd_a == 0:
                return 0
        return gcd_a
    else:
        for num in arrayB:
            if num % gcd_a == 0:
                isMod_a = True
                break
        for num in arrayA:
            if num % gcd_b == 0:
                isMod_b = True
                break
        if isMod_a and isMod_b: return 0
        if isMod_a:
            if not isMod_b: return gcd_b
        if isMod_b:
            if not isMod_a: return gcd_a
        if not isMod_a and not isMod_b: return max(gcd_a, gcd_b)
        
    return answer