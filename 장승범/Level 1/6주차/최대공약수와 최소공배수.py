import math

def solution(n, m):
    
    return [math.gcd(n, m), (n * m) // math.gcd(n, m)]


'''
def solution(n, m):
    
    a, b = max([n, m]), min([n, m])
    
    while b:
        a, b = b, a % b
    
    return[a, int(n * m / a)]
'''