import datetime

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    answer = datetime.datetime(2016, a, b).weekday()
    
    return days[answer]
