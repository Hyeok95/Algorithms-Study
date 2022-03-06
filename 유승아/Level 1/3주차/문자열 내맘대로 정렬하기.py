def solution(strings, n):
    # x[n]을 기준으로만 정렬하면, n번째 알파벳이 동일한 경우를 처리하지 못함
    answer = sorted(strings, key= lambda x: (x[n], x))
    return answer