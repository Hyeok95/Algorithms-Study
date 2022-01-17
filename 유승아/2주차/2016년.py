import datetime

def solution(a, b):
    info = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    
    return info[datetime.date(2016,a,b).weekday()]