def solution(a, b):
    answer = 0
    c = sorted([a, b])

    for i in range(c[0], c[-1]+1):
        answer += i
    
    return answer