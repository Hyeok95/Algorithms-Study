
def solution(n):
    
    THR = ''
    
    while n > 1:
        THR = str(n % 3) + THR
        n = n // 3
    
    if n == 1:
        THR = '1' + THR
    
    answer = 0
    j = 1
    
    for i in THR:
        answer += int(i) * j
        j = j * 3
    
    
    return answer