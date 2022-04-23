def solution(numbers):
    answer = ''
    # 숫자 -> 문자열로 변경
    numbers = list(map(str, numbers))
    # 문자열 3 vs 30 에서 30이 우선순위를 가지는것을 막기위해, 문자열을 세번씩 반복해준다(3인 이유는 30, 300에서도 똑같은 문제가 발생하는데, 해당 문제는 1000이하의 숫자로 제한이 되있기 때문)
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    for i in numbers:
        answer += i
    
    return answer