def solution(numbers):
    num = set(range(10))
    return sum(num - set(numbers))