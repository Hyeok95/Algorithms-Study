import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        count +=1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return count