from itertools import combinations

def solution(numbers):
    answer = []
    temp = combinations(numbers, 2)
    for t in temp:
        answer.append(sum(t))
    return sorted(set(answer))