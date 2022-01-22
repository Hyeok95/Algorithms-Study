import itertools

def solution(numbers):

    result = []
    
    for i in range(1, len(numbers) + 1):
        n_list = list(map(lambda x : int("".join(x)), itertools.permutations(list(numbers), i)))
        for i in set(n_list):
            temp = 0
            if i == 1:
                continue
            for j in range(1, int(i ** 0.5) + 1):
                if temp > 1:
                    break
                elif i % j == 0:
                    temp += 1

            if temp == 1 and i not in result:
                result.append(i)
    
    return len(result)


'''
permutatation, 에라토스테네스 체 set 사용

from itertools import permutations

def solution(n):
    a = set()
    for i in range(len(n)):
        a |= set(map(int, map("".join, permutations(list(n), i + 1))))
    
    a -= set(range(0, 2)) # 0, 1 제외 및 중복 제거
    
    for i in range(2, int(max(a) ** 0.5) + 1):
        a -= set(range(i * 2, max(a) + 1, i)) # 소수 이외 수 제거 <깔끔>
    
    return len(a)

'''