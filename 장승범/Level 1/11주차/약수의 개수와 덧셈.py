
def solution(left, right):
    
    answer = 0
    
    for i in range(left, right + 1):
        cnt = 0
        if i % (i ** 0.5) == 0:
            answer -= i
        else:
            answer += i

                
    return answer