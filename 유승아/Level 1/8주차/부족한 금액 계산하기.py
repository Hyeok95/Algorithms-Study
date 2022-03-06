def solution(price, money, count):
    temp = 0
    for i in range(count):
        temp += price *(i+1)
        
    return 0 if temp <= money else temp-money