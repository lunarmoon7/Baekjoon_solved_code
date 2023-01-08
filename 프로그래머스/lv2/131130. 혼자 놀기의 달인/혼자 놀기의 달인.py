ret = []
def solution(cards):
    n = len(cards)
    
    # for start in range(n):
    isPicked = [False for _ in range(n)]
    for start in range(n):
        if not isPicked[start]:
            helper(cards, isPicked, start, [])
    ret.sort(key=lambda x: len(x), reverse=True)
    answer = 0 if len(ret) == 1 else len(ret[0]) * len(ret[1])
    return answer
def helper(cards, isPicked, idx, group):
    global ret
    if isPicked[idx]:
        # ret.append(len(group))
        ret.append(group)
        return
    isPicked[idx] = True
    helper(cards, isPicked, cards[idx] - 1, group + [cards[idx]])
            
    
    
