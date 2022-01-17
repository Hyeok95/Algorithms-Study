from math import gcd

def solution(n, m):
    answer = []
    answer.append(gcd(n,m)) #최대공약수
    answer.append(n*m // gcd(n,m)) #최소공배수
    return answer