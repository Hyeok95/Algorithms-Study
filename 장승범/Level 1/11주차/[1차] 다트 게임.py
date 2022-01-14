
def solution(dartResult):
    
    answer = []
    
    score_dict = {'S': 1, 'D': 2, 'T': 3}
    
    for i in range(len(dartResult)):
        try:
            try:
                if type(int(dartResult[i - 1])) == int:
                    answer[-1] = answer[-1] * 10 + int(dartResult[i])
                else:
                    answer.append(int(dartResult[i]))
            except:
                answer.append(int(dartResult[i]))
            
        except:
            if dartResult[i] in score_dict:
                answer[-1] = answer[-1] ** score_dict[dartResult[i]]
            elif dartResult[i] == '*':
                if len(answer) == 1:
                    answer[-1] = answer[-1] * 2
                else:
                    answer[-1] = answer[-1] * 2
                    answer[-2] = answer[-2] * 2
            else:
                answer[-1] = answer[-1] * (-1)
    
    return sum(answer)