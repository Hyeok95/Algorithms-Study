def solution(n):
    
    a = n ** (1/2)
        
    if a == int(a):
        return (a + 1) ** 2
    else:
        return -1