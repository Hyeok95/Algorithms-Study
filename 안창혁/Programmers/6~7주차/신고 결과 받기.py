def solution(id_list, report, k):
    dict = {name : [] for idx, name in enumerate(id_list)} #신고한 사람
    reports = {name:0 for i, name in enumerate(id_list)} #신고받은 횟수
    
    for i in set(report):
        user = i.split(" ")[0]
        reported_user = i.split(" ")[1]
        dict[user].append(reported_user)
        reports[reported_user] +=1        
    
    answer = [0 for i in range(len(id_list))]
    for key, values in dict.items():
        for value in values:
            if reports[value] >=k:
                answer[id_list.index(key)] += 1
    
    return answer