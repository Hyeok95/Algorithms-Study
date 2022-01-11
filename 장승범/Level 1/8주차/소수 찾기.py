def solution(n):

    result = [False] + [True] * n
    
    for i in range(2, int(n ** 0.5) + 1):
        if result[i] == True:
            for j in range(i + i, n + 1, i):
                result[j] = False
    
    return result.count(True) - 1

'''
에라토스테네스의 체 풀이

def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    
    return len(num)

'''
