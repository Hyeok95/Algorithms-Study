def solution(n, lost, reserve):
    
    #set 함수를 쓰는 이유 : 리스트는 - 연산이 되지않으므로 set연산을 쓴다.
    lost_n = set(lost) - set(reserve)
    reserve_n = set(reserve) - set(lost)
    
    for i in reserve_n:
        if i-1 in lost_n:
            lost_n.remove(i-1)
        elif i+1 in lost:
            lost_n.remove(i+1)
        
    return n-len(lost_n)
