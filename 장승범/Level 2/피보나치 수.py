def solution(n):
    fibo = {0 : 0, 1 : 1, 2 : 1}
    
    if n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n + 1):
            fibo[i] = fibo[i - 1] + fibo[i - 2]
    
    return fibo[n] % 1234567