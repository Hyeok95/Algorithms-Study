def solution(n):
    temp = list(str(n))
    return int(''.join(sorted(temp, reverse = True)))