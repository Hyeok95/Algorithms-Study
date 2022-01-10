def solution(answers):
    answer = []
    one = 1, 2, 3, 4, 5
    two = 2, 1, 2, 3, 2, 4, 2, 5
    three = 3, 3, 1, 1, 2, 2, 4, 4, 5, 5
    score = [0,0,0]
    result = []
    
    for i ,v in enumerate(answers):
        if v == one[i%len(one)]:
            score[0] += 1
        if v == two[i%len(two)]:
            score[1] += 1
        if v == three[i%len(three)]:
            score[2] += 1
    
    for i,s in enumerate(score):
        if s == max(score):
            result.append(i+1)
    return result