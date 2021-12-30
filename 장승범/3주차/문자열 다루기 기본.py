import re

def solution(s):
    
    s = re.sub('[a-zA-Z]','false',s)
    
    if len(s) != 4 and len(s) != 6:
        return False
    elif 'false' in s:
        return False
    else:
        return True