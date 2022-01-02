'''

def solution(n):
    
    return n + sum([i for i in range(1, n // 2 + 1) if n % i == 0])

'''


def solution(n):
    
    divisor = 0
    
    i = 1
    
    while i * i <= n:
        if n % i == 0:
            if i == (n / i):
                divisor += i 
            else:
                divisor += (i + n / i)
        
        i += 1
    
    
    return divisor