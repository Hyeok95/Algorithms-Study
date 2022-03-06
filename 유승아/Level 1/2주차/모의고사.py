def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    
    score = dict()
    for i in range(3):
        score[i+1] = 0
    
    for i in range(len(answers)):
        if one[i%5] == answers[i]:
            score[1] += 1  
        if two[i%8] == answers[i]:
            score[2] +=1 
        if three[i%10] == answers[i]:
            score[3] +=1
           
    answer = [k for k,v in score.items() if max(score.values()) == v ]
    
    return answer