import math
def solution(n, m):
    gcd = math.gcd(n,m)
    for i in range(max(n,m), (n*m + 1)):
        if i % n == 0 and i % m ==0:
            lcm = i
            break
    
    return [gcd,lcm]