def solution(progresses, speeds):
    answer = []
    
    # progresses의 원소가 100이 넘으면 pop
    while progresses:
        for i in range(len(progresses)):
            # 진행상황 업데이트
            progresses[i] += speeds[i]
        
        count = 0 # 초기화
        
        # 진행해야하는 일들이 남아있고, 제일 앞에 있는 기능이 완성된 경우
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count +=1
        
        if count > 0:
            answer.append(count)
    
    return answer