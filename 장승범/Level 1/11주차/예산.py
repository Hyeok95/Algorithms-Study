
def solution(d, budget):
    d.sort()
    cnt = 0
    for i in d:
        budget -= i
        if budget >= 0:
            cnt += 1
    
    return cnt