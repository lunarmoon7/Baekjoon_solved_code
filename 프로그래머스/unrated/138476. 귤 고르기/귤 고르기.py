import collections

def solution(k, tangerine):
    # sol 1
#     answer = 0
#     hashmap = collections.defaultdict(int)
    
#     for i in tangerine:
#         hashmap[i] += 1
    
#     hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    
#     for key, val in hashmap:
#         if k <= 0: break
#         k -= val
#         answer += 1
        
    
#     return answer
    # sol 2
    answer = 0
    c = collections.Counter(tangerine)
    sort_list = sorted(c.values(), reverse=True)
    for v in sort_list:
        k -= v
        answer += 1
        if k <= 0: break
    return answer