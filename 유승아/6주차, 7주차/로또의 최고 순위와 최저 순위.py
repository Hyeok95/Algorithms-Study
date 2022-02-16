def solution(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]
    value = lottos.count(0)
    count = 0
    
    for x in sorted(lottos, reverse=True):
        if x in win_nums:
            count += 1
    
    
    return [rank[count+value], rank[count]]