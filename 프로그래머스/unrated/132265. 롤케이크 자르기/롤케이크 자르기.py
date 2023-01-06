from collections import Counter
def solution(topping):
    # TLE
#     answer = 0
#     n = len(topping)
#     for i in range(n):
#         c1 = Counter(topping[:i])
#         c2 = Counter(topping[i:])
#         if len(c1) == len(c2): answer += 1
        
#     return answer
    answer = 0
    hashmap = Counter(topping)
    s = set()
    for t in topping:
        hashmap[t] -= 1
        s.add(t)
        if hashmap[t] == 0:
            hashmap.pop(t)
        if len(hashmap) == len(s): answer += 1
    return answer