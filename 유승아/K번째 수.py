def solution(array, commands):
    answer = []
    for list in commands:
        
        i, j, k = list[0], list[1], list[2]
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])        
          
    return answer