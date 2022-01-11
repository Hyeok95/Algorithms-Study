def solution(lottos, win_nums):
    
    cnt = 0
    num_Z = lottos.count(0)
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
    
    answer = []
    
    lt_list = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    return [lt_list[cnt + num_Z], lt_list[cnt]]