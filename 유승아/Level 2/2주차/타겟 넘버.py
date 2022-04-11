def solution(numbers, target):
    answer = 0
    
    # 첫번째 시작 숫자,  +,- 두가지 경우
    cases = [[numbers[0],0], [-1*numbers[0],0]]
    
    n = len(numbers)
    
    while cases:
        temp, idx = cases.pop()
        idx += 1
        
        # 경우의 수 만들기
        if idx < n:
            cases.append([temp+numbers[idx], idx])
            cases.append([temp-numbers[idx], idx])
        
        # 모든 케이스를 만든 후 확인
        else:
            if temp == target:
                answer += 1
    
    # 모든 경우의 수를 확인하고 리턴
    return answer