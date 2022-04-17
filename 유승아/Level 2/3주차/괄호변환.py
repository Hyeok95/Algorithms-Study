# 잘못된 문자열인 경우 새로운 문자열을 만드는 방법에 대한 아이디어가 없음

def divide(p):
    open = 0
    close = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i+1], p[i+1:]
        
def check(u):
    temp = []
    for p in u:
        if p =='(':
            temp.append(p)
        else:
            if len(temp) == 0:
                return False
#           빼낼 괄호가 있는경우에만 POP
            temp.pop()
    return True

def solution(p):
    answer = ''
    return answer