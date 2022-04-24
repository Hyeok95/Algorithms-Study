def solution(phoneBook):
    phoneBook.sort()
    
    # 정렬을 통해 인접한 숫자들은 비슷한 번호로 시작이 되도록 만들어 놨음.
    # zip 함수를 이용하여 두개의 번호를 엮고, 
    # 인덱싱을 통해 인접한 번호들끼리 비교하도록 설정
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True