def solution(a, b):
    
    answer = 0
    
    array = sorted([a, b])
    
    for i in range(array[0], array[1] + 1):
        answer += i
        
    return answer