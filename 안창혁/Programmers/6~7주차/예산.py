def solution(d, budget):
    answer = 0
    count = 0
    s = sorted(d)
    
    for i in s:
        answer += i
        if answer <= budget:
            count += 1
    
    return count