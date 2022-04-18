def solution(s):
    answer = []
    # 밖에있는 {{}}를 없애준다.
    s = s[2:-2]
    # 숫자만 빼서 리스트 형태로 저장한다.
    s = s.split("},{")
    
    # 오름차순 정렬
    s.sort(key = len)
    
    for i in s:
        i_list = i.split(',')
        for j in i_list:
            # 기존에 추가된 숫자 거르기
            if int(j) not in answer:
                answer.append(int(j))
    return answer