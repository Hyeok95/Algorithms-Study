def solution(n):
    answer = ''
    if n <= 3:
        return '124'[n-1]
    else:
        a, b = divmod(n-1, 3)
        answer += solution(a) + '124'[b]
        
    return answer