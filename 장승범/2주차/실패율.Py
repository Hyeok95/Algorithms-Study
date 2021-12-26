def solution(N, stages):
    
    result = []
    
    for i in range(N):
        f_rate = stages.count(i + 1) / len([x for x in stages if x >= i + 1])
        result.append(f_rate)
    
    desc_result = sorted(result, reverse=True) 

    fin_result = []

    for i in desc_result: 
        if len(fin_result) == 0 or i != result[fin_result[-1] - 1]:
            fin_result.append(result.index(i) + 1)
        else:
            fin_result.append(fin_result[-1] + 1)
    
    return fin_result

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))