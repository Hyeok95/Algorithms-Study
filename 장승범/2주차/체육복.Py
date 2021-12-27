def solution(n, lost, reserve):

    mod_lost = list(set(lost) - set(reserve))
    mod_reserve = list(set(reserve) - set(lost))
    
    for i in mod_lost:
        if i - 1 in mod_reserve:
            mod_reserve.remove(i - 1)
        elif i + 1 in mod_reserve:
            mod_reserve.remove(i + 1)
        else:
            n -= 1
    
    return n