def solution(record):
    answer = []
    
    # id 와 최종 nickname을 저장하는 딕셔너리
    id_name = {}
    for message in record:
        temp = message.split(" ")
        # 들어올 때, 닉네임 변경했을 때 딕셔너리값 변경
        if len(temp) == 3:
            id_name[temp[1]] = temp[2]
           
    for message in record:
        temp = message.split(" ")
        if temp[0] == "Enter":
            answer.append(f'{id_name[temp[1]]}님이 들어왔습니다.')
        elif temp[0] == "Leave":
            answer.append(f'{id_name[temp[1]]}님이 나갔습니다.')
            
    return answer