def solution(n):
    answer = []
    
    for i in range(1, n):
        if n % i == 1:
            answer.append(i)
    
    result = answer[0] 
    return result