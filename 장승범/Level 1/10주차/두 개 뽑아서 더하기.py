
import itertools

def solution(numbers):
    result = list(itertools.combinations(numbers, 2))
    
    
    answer = []
    for i in result:
        if sum(i) not in answer:
            answer.append(sum(i))
    
    answer.sort()
    
    return answer