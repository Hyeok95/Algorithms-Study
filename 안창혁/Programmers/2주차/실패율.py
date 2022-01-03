def solution(N, stages):
    answer = {}
    
    stage = len(stages)
    
    for i in range(1, N+1):
        if stage != 0:
            count = stages.count(i)
            answer[i] = count / stage
            stage -= count
        else:
            answer[i] = 0
    
    return sorted(answer, key=lambda x: answer[x], reverse=True)
