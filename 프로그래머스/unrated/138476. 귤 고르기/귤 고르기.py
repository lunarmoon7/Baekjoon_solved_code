import collections

def solution(k, tangerine):
    answer = 0
    hashmap = collections.defaultdict(int)
    
    for i in tangerine:
        hashmap[i] += 1
    
    hashmap = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
    
    for key, val in hashmap:
        if k <= 0: break
        k -= val
        answer += 1
        
    
    return answer