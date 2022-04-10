def solution(x):
    # 숫자 -> 문자 -> 리스트 -> 합 -> x로 나눠지는지 확인
    str_x = str(x)
    num_list = [int(i) for i in str_x]
    return True if x % sum(num_list) == 0 else False