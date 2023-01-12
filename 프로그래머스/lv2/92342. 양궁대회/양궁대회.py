import copy
max_diff = 0
answer = []
def calcDiff(info, shots):
    apeach_sum, rion_sum = 0, 0
    for i in range(11):
        if (info[i], shots[i]) == (0, 0): continue
        if info[i] >= shots[i]:
            apeach_sum += 10 - i
        else:
            rion_sum += 10 - i
    return rion_sum - apeach_sum
def dfs(n, info, shots, idx):
    global max_diff, answer
    if idx == 11:
        if n != 0:
            shots[10] = n
        score_diff =calcDiff(info, shots)
        if score_diff <= 0:
            return
        ret = copy.deepcopy(shots)
        if score_diff > max_diff:
            max_diff = score_diff
            answer = [ret]
            return
        if score_diff == max_diff:
            answer.append(ret)
        return 
    if info[idx] < n:
        dfs(n - info[idx] - 1, info, shots + [info[idx] + 1], idx + 1)    
    dfs(n, info, shots + [0], idx + 1)

def solution(n, info):
    global max_diff, answer
    dfs(n, info, [], 0)
    if not answer: return [-1]
    answer.sort(key = lambda x : x[::-1], reverse=True)
    return answer[0]

    

    