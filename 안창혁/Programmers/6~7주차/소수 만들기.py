# combination() 사용 : 중복을 허용하지 않고, 순서 의미가 있는 조합을 리턴해준다.
from itertools import combinations

def check(a): 
    for i in range(2, a): 
        if a % i == 0 :
            return False 
    return True

def solution(nums):
    count = 0
    comb = list(combinations(nums,3))
    
    for arr in comb:
        if check(sum(arr)):
            count += 1
        
    return count