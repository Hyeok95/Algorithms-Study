
def solution(new_id):

    new_id = new_id.lower() # 필터 1 소문자로 변환

    letters_filter ='~!@#$%^&*()=+[{]}:?,<>/'

    mod_id = ''

    for i in new_id: # 필터 2 알파벳 소문자, 숫자, '-', '_', '.' 이외 제거
        if i not in letters_filter:
            mod_id += i

    while '..' in mod_id: # 필터 3 마침표(.) 2번 이상 연속된 부분 마침표 하나로 치환
        mod_id = mod_id.replace('..', '.')
    
    mod_id = list(mod_id)

    if mod_id[0] == '.':
        mod_id[0] = ' '
    
    if mod_id[-1] == '.':
        mod_id[-1] == ' '
    
    while ' ' in mod_id:
        mod_id.remove(' ')
    
    if len(mod_id) == 0:
        mod_id = ['a']

    if len(mod_id) > 15: # 길이 15로 변경, 마지막 문자 '.' 일 경우 제거
        mod_id = mod_id[:15]
    
    if mod_id[-1] == '.':
        del mod_id[-1]
            
    while len(mod_id) < 3:
        mod_id.append(mod_id[-1])

    return ''.join(mod_id)

print(solution(input()))

