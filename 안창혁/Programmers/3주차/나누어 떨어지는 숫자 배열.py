def solution(arr, divisor):
    answer = []
    temp = []
    
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
        elif i % divisor != 0:
            temp.append(i)
            if len(temp) == len(arr):
                return [-1]
    
    return answer