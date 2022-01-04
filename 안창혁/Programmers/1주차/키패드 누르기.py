def solution(numbers, hand):
    answer = ''
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += "L"
        if i == 3 or i == 6 or i == 9:
            answer += "R"
    return answer
