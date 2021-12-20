'''
정규식 사용

import re

def solution(new_id):

    st = new_id.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('[.]$', '', st)
    st = st if len(st) > 2 else st + ''.join([st[-1] for i in range(3-len(st))])
    return st
'''


def solution(new_id):

    new_id = new_id.lower() # 필터 1 소문자로 변환

    letters_filter ='~!@#$%^&*()=+[{]}:?,<>/' # 필터 2 알파벳 소문자, 숫자, '-', '_', '.' 이외 제거

    mod_id = ''

    for i in new_id: 
        if i not in letters_filter:
            mod_id += i

    while '..' in mod_id: # 필터 3 마침표(.) 2번 이상 연속된 부분 마침표 하나로 치환
        mod_id = mod_id.replace('..', '.')
    
    if mod_id[0] == '.': # 필터 4
        mod_id = mod_id[1:] if len(mod_id) > 1 else '.'

    if mod_id[-1] == '.':
        mod_id = mod_id[:-1]
    
    if len(mod_id) == 0: # 필터 5
        mod_id = 'a'

    if len(mod_id) > 15: # 필터 6 길이 15로 변경, 마지막 문자 '.' 일 경우 제거
        mod_id = mod_id[:15]
        if mod_id[-1] == '.':
            mod_id = mod_id[:-1]
            
    while len(mod_id) < 3: # 필터 7
        mod_id += mod_id[-1]

    return mod_id
