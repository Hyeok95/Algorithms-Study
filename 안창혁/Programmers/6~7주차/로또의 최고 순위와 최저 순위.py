def solution(lottos, win_nums):
    answer = [0,0]
    rank = [6,6,5,4,3,2,1]
    count = 0
    max_count = lottos.count(0)
    
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
        
    answer[0] = rank[count+max_count]
    answer[1] = rank[count]
    return answer