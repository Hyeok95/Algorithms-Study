def solution(record):
    name_dict = {}
    
    answer = []

    for i in record:
        if i.split()[0] == 'Enter':
            name_dict[i.split()[1]] = i.split()[2]
            answer.append([i.split()[1], "님이 들어왔습니다."])
        elif i.split()[0] == 'Leave':
            answer.append([i.split()[1], "님이 나갔습니다."])
        else:
            name_dict[i.split()[1]] = i.split()[2]
            
    answer = list(map(lambda x : name_dict[x[0]] + x[1] , answer))
    
    return answer
