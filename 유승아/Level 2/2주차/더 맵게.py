import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # heap으로 변경
    
    # 가장 낮은 스코빌지수가 K보다 커지면 더이상 섞을 필요 없음
    while scoville[0] < K and len(scoville) > 1:
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        
        # 스코필 지수가 가장 낮은 두개의 음식을 섞음
        heapq.heappush(scoville, a + (b * 2))
        answer +=1
        
        # 섞을 음식이 더이상 없을때, 최대로 낼수있는 매운맛이 K를 넘지못할때 -1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer