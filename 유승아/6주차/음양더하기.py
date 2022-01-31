def solution(absolutes, signs):
    sum = 0
    for a in zip(absolutes, signs):
        if a[1] == True:
            sum += a[0]
        else:
            sum -= a[0]
    return sum