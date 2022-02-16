def solution(price, money, count):
    
    Sum = 0
    for i in range(1, count+1):
        Sum += (price*i)
    
    if money < Sum:
        return Sum - money
    else:
        return 0