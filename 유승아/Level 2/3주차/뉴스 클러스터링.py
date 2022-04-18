# 자카도 유사도
from collections import Counter

def solution(str1, str2):
    # 뉴스 제목을 소문자로 모두 바꾼다.
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 두글자크기의 다중집합을 저장해줄 리스트
    str1_list = []
    str2_list = []
    
    # 두글자씩 끊어서 다중집합 확인
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            str1_list.append(str1[i]+ str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            str2_list.append(str2[i]+ str2[i+1])
    
    # 다중집합의 개수를 세줌
    count1 = Counter(str1_list)
    count2 = Counter(str2_list)
    print(count1, count2)

    # 문자열간의 교집합과 합집합을 구한다
    inter = list((count1 & count2).elements())
    union = list((count1 | count2).elements())
    
    if len(union) == 0 and len(inter) == 0:
        return 65536
    else:
        # 교집합 크기를 두 집합의 합집합 크기로 나눈 값 -> 자카드 유사도
        return int(len(inter) / len(union) * 65536)