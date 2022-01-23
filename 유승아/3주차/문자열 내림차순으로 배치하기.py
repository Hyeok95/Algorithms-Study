def solution(s):
    answer = ''
    for t in sorted(s, reverse=True):
        answer +=t
    
    return answer