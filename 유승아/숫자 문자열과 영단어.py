def solution(s):
    digit_dict = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    result = ''
    temp =''
    for a in s:
        if a.isdigit():
            result += a
        else:
            temp += a
            if temp in digit_dict.keys():
                result += digit_dict[temp]
                temp = ''
    return int(result)
