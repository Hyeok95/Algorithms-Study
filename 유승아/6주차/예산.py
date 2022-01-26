def solution(d, budget):
    answer = 0
    d.sort()
    for need in d:
        if need <= budget: 
            answer +=1
            budget -= need
        else:
            break
    return answer