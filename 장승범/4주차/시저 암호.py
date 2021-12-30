def solution(s, n):
    
    alpha = 'abcdefghijklmnopqrstuvwxyz' * 2
    
    result = ''
    
    for i in s:
        if i == ' ':
            result += ' '
        elif i.isupper():
            result += alpha[alpha.index(i.lower()) + n].upper()
        else:
            result += alpha[alpha.index(i) + n]
    
    
    return result