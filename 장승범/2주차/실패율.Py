def solution(N, stages):
    f_list = {}
    players = len(stages)

    for i in range(1, N + 1):
        if players != 0:
            n_stage = stages.count(i)
            f_list[i] = n_stage / players
            players -= n_stage
            
        else:
            f_list[i] = 0
            
    return sorted(f_list, key = lambda x : f_list[x], reverse = True)