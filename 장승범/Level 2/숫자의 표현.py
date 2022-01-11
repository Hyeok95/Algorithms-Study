def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        temp = i
        a = i
        while temp < n + 1:
            if temp == n:
                cnt += 1
                break
            else:
                a += 1
                temp += a
        
    return cnt