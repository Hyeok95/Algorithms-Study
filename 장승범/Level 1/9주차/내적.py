def solution(a, b):
    cnt = 0
    for i in range(len(a)):
        cnt += a[i] * b[i]
    return cnt