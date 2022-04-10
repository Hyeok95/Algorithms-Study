def solution(s):
    answer = -1
    check_stack = []
    
    for i in s:
        # check_stack에 아무값도 없는 경우, 추가 
        if len(check_stack) == 0:
            check_stack.append(i)
        # check_stack에 있는 값이, 현재의 문자열과 똑같은 경우 check_stack에서 제거 
        elif check_stack[-1] == i:
            check_stack.pop()
        # check_stack의 마지막 값이, 현재 문자열과 다른 경우 추가    
        else:
            check_stack.append(i)
    
    # 모든 문자열이 삭제되는 경우
    if len(check_stack) == 0:
        return 1
    
    return 0