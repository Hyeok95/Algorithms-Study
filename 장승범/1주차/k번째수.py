def solution(array, commands):
    
    result = []
    
    for i in commands:
        temp = sorted(array[i[0] - 1 : i[1]])
        
        result.append(temp[i[2] - 1])

    return result