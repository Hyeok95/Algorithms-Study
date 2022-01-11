def solution(arr):
    
    result = []
    
    for i in arr:
        if len(result) == 0:
            result.append(i)
        else:
            if result[-1] != i:
                result.append(i)
    
    return result


#  [:-1] 빈 array에도 적용 가능
# def solution(arr):
#     result = []
#     for i in arr:
#         if result[-1:] == [i]: 
#             continue
#         result.append(i)

#     return result
