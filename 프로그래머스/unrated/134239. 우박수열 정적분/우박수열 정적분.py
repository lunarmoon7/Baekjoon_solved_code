def collatz(k):
    points = [k]
    while k != 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = 3 * k + 1
        points.append(k)
    return points
def solution(k, ranges):
    answer = []
    n = len(ranges)
    points = collatz(k)
    
    for s, e in ranges:
        e = len(points) + e - 1
        if s > e:
            answer.append(-1)
        else:
            total = 0
            for i in range(s, e):
                first = points[i]
                second = points[i + 1]
                total += (first + second) / 2
            answer.append(total)
    return answer