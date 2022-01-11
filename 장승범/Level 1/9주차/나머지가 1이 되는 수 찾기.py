def solution(n):
    
    for i in range(2, int((n - 1) ** 0.5) + 1):
        if (n - 1) % i == 0:
            return i
        
    return n - 1