def solution(a, b):
    
    Days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    
    n_Days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if a == 1:
        return Days[b % 7 - 1]
    
    else:
        return Days[(sum(n_Days[:a - 1]) + b) % 7 - 1]
