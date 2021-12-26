def solution(n, lost, reserve):

    lost.sort()
    
    for i in lost:
        if i in reserve:
            reserve.remove(i)
        elif i - 1 in reserve and i - 1 not in lost:
            reserve.remove(i - 1)
        elif i + 1 in reserve and i + 1 not in lost:
            reserve.remove(i + 1)
        else:
            n -= 1
    
    return n