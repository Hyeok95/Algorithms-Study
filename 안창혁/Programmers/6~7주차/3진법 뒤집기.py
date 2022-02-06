def solution(n):
    answer = ""
    
    while n:
        answer += str(n % 3)
        n = n // 3
    
    result = int(str(answer),3)
    
    return result