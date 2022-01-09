def solution(nums):
    set_num = set(nums)  # 중복 폰켓몬 제거
    answer = min(len(set_num), len(nums)//2)  
    return answer