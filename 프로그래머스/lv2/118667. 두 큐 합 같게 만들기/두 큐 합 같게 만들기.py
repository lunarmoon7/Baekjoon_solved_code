from collections import deque
def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    s1, s2 = sum(queue1), sum(queue2)
    if (s1 + s2) % 2 != 0: return -1
    
    while True:
        if s1 > s2:
            curr = queue1.popleft()
            queue2.append(curr)
            s1 -= curr
            s2 += curr
            answer += 1
        elif s1 < s2:
            curr = queue2.popleft()
            queue1.append(curr)
            s2 -= curr
            s1 += curr
            answer += 1
        else:
            break
        if answer == len(queue1) * 4: return -1
        
    return answer