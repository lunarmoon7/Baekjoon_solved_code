def solution(elements):
    # sol 1 - 너무 느림
    seq_set = set()
    n = len(elements)
    elements += elements
    
    for k in range(1, n + 1):
        for i in range(n):
            seq_set.add(sum(elements[i:i + k]))
    return len(seq_set)