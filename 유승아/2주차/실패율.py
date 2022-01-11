def solution(N, stages):
    answer = dict()
    people = len(stages)  # 사용자 수 
    for i in range(1, N+1):
        if stages.count(i) != 0:   # 도전중인 사용자가 있는지 확인
            answer[i] = stages.count(i)/people  # 도전중인 사용자/stage에 온 사람
            people -= stages.count(i)           # 도전중인 사용자들은 다음 stage에 갈 수 없음
        else:                      # 도전중인 사용자가 없다면, 실패율 0
            answer[i] = 0
        
    return sorted(answer, key = lambda x: answer[x], reverse=True)