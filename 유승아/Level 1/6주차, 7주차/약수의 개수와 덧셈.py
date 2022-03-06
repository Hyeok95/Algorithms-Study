def solution(id_list, report, k):
    result_dict = {id: [] for id in id_list}
    answer = [0] * len(id_list)
    
    for r in set(report):
        a, b = r.split(" ")
        result_dict[b].append(a)
        
    for key, values in result_dict.items():
        if len(values) >= k:
            for v in values:
                answer[id_list.index(v)] +=1    
    return answer
    