def solution(s):
    answer = ''
    for idx, alpha in enumerate(s):
        if idx % 2 == 0:
            alpha = alpha.upper()
            answer += alpha
        elif idx % 2 == 1:
            alpha = alpha.lower()
            answer += alpha
            
    return answer