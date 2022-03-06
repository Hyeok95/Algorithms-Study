def solution(n):
    a = "수박"
    
    if n % 2 == 0:
        return a * (n // 2)
    return a *(n // 2) + a[0]