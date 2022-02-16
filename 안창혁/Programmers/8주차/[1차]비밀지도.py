def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        temp = bin(arr1[i] | arr2[i])
        temp = temp[2:].zfill(n)
        temp = temp.replace("1", "#").replace("0", " ")
        answer.append(temp)
    
    return answer