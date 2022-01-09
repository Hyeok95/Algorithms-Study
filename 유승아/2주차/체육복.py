def solution(n, lost, reserve):
    answer = []
    set_lost = set(lost)-set(reserve)       # 체육복이 0개인 경우
    set_reserve = set(reserve)-set(lost)    # 여분의 체육복이 있는 경우

    answer = n-len(set_lost)                # 체육복이 준비된 학생의 수 
    
    for i in set_lost:
        if i-1 in set_reserve:              # 앞번호 학생에게 체육복을 빌릴 수 있는 경우
            set_reserve.remove(i-1)
            answer +=1
        elif i+1 in set_reserve:            # 뒷번호 학생에게 체육복을 빌릴 수 있는 경우
            set_reserve.remove(i+1)
            answer +=1
    return answer