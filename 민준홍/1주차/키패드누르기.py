# 내풀이

def solution(numbers, hand):
    answer = ''
    right_registed_nums = ''
    left_registed_nums = ''
    left = 1, 4, 7
    right = 3, 6, 9
    mid = 2, 5, 8, 0

    for i in range(len(numbers)):
        if numbers[i] in left:
            answer += "L"
            left_registed_nums += str(numbers[i])
        elif numbers[i] in right:
            answer += "R"
            right_registed_nums += str(numbers[i])
            # 2580 만들기 실패
        else:
            if numbers[i] + 1 == left_registed_nums[-1] or numbers[i] - 1 == right_registed_nums[-1]:
                if hand == "left":
                    answer += "L"
                else:
                    answer += "R"

    return answer
# 베스트 코딩


def solution(numbers, hand):
    answer = ''
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    left = [1, 4, 7]
    right = [3, 6, 9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
            # 2580 만들기 코딩
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
 
            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
