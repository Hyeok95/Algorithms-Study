import calendar

def solution(a, b):
    week_list = ["MON","TUE","WED","THU","FRI","SAT","SUN"]
    day = calendar.weekday(2016, a, b)
    answer = week_list[day]
    return answer