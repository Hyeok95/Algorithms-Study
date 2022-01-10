def solution(a, b):
    answer = 0
    for i in range(min(a,b),max(a,b)+1):
        answer += i
    return answer

#수학공식 S=(∣a−b∣+1)∗(a+b)/2 적용하면

#(abs(a-b)+1)*(a+b)/2 이런식도 도출 가능!!