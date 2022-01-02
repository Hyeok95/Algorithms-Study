def solution(s):
    
    result = ''
    
    index = 0
    
    for i in s:
        if i == ' ':
            result += ' '
            index = 0
        elif index % 2 == 0:
            result += i.upper()
            index += 1
        else:
            result += i.lower()
            index += 1
        
    return result

print(solution("try hello world"))