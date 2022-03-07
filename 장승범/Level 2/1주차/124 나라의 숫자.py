def solution(n):
    
    answer = ''
    base_3 = '124'
    
    while 1:
        if n > 3:
            answer += base_3[(n % 3) - 1]
            n = (n - 1) // 3
        else:
            answer += base_3[(n % 3) - 1]
            break ;
    
    return answer[::-1]