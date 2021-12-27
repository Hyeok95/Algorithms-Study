def Distance(handNumber, nextNumber):
    keypad = {1: [0, 0], 2: [1, 0], 3: [2, 0],
              4: [0, 1], 5: [1, 1], 6: [2, 1],
              7: [0, 2], 8: [1, 2], 9: [2, 2],
              "*": [0, 3], 0: [1, 3], "#": [2, 3], }

    x1, y1 = keypad[handNumber]
    x2, y2 = keypad[nextNumber]

    return abs(x1-x2) + abs(y1-y2)

def solution(numbers, hand):
    answer = ''
    l,r = '*', '#'
    if hand == 'right':
        hand = 'R'
    else:
        hand = 'L'
    
    for i in numbers:
        if i in [1, 4, 7]:
            answer += 'L'
            l = i
        elif i in [3, 6, 9]:
            answer += 'R'
            r = i
        else:
            # 거리구하기
            ld = Distance(l, i)
            rd = Distance(r, i)
            if ld < rd :
                answer += 'L'
                l = i
            elif ld > rd:
                answer += 'R'
                r = i
            else:
                if hand == "R":
                    answer += 'R'
                    r = i
                else:
                    answer += 'L'
                    l = i

    
    return answer
