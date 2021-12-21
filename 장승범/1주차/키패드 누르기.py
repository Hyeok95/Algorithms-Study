def solution(numbers, hand):
    
    key_pad = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
        }
    
    right_hand = key_pad['*'] # [3, 0] 세팅
    left_hand = key_pad['#'] # [3, 2] 세팅
    
    result = ''
    
    for i in numbers:
        if i in [1, 4, 7]:
            result += 'L'
            left_hand = key_pad[i]
        elif i in [3, 6, 9]:
            result += 'R'
            right_hand = key_pad[i]
        else:
            from_R = abs(key_pad[i][0] - right_hand[0]) + abs(key_pad[i][1] - right_hand[1])
            from_L = abs(key_pad[i][0] - left_hand[0]) + abs(key_pad[i][1] - left_hand[1])
            
            if from_R < from_L:
                result += 'R'
                right_hand = key_pad[i]
            elif from_R > from_L:
                result += 'L'
                left_hand = key_pad[i]
            else:
                if hand == 'right':
                    result += 'R'
                    right_hand = key_pad[i]
                else:
                    result += 'L'
                    left_hand = key_pad[i]
            
    return result