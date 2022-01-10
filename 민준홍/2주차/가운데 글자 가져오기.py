def solution(s):
    answer = ''
    mid = len(s)//2
    if len(s)%2 == 0:
        answer += s[mid-1:mid+1]
    else:
        answer += s[mid]
    return answer