def solution(s):
    answer = ''
    check = len(s)
    
    if check % 2 ==0:
        answer += (s[check//2-1])
    answer += (s[check//2])
    
    return answer