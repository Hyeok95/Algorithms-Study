from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque([(v,i) for i,v in enumerate(priorities)])
    
    while q:
        val = q.popleft()
        if q and val[0] < max(q)[0]:
            q.append(val)
        else:
            answer += 1
            if val[1] == location:
                break
        
    return answer