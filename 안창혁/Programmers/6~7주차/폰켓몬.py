def solution(nums):
    answer=0
    n = len(nums)//2
    print(set(nums))
    
    if len(list(set(nums)))>n:
        answer=n
    else:
        answer=len(list(set(nums)))
    return answer