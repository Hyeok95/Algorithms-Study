def solution(s):
    
    upper = ''
    lower = ''
    
    for i in s:
        if i.isupper == True:
            upper += i
        else:
            lower += i
    
    upper = sorted(upper, reverse=True)
    lower = sorted(lower, reverse=True)
    
    return ''.join(lower + upper)