import collections

def solution(nums):
    
    cns = int(len(nums) / 2)
    
    nums = list(collections.Counter(nums))
    
    if cns <= len(nums):
        return cns
    else:
        return len(nums)
    