def solution(progresses, speeds):
    answer = []
    temp = [0] * len(progresses)
    
    while (True):
        count = 0
        for i in range(len(progresses)):
            if progresses[i] < 100:
                progresses[i] += speeds[i]
                temp[i] += 1
            else:
                count += 1
        if count == len(progresses):
            break
    
    max_days = 0
    for i in temp:
        if i > max_days:
            answer.append(1)
            max_days = i
        else:
            answer[-1] += 1
            
    return (answer)