import itertools

def isPrime(A):
    if A % 2 == 0 or A % 3 == 0:
        return False
    else:
        for i in range(3, int(A ** 0.5) + 1, 2):
            if A % i == 0:
                return False

    return True
        
def solution(nums):
    
    n_list = []
    
    for i in itertools.combinations(nums, 3):
        n_list.append(sum(i))
    
    cnt = 0
    
    for j in n_list:
        if isPrime(j):
            cnt += 1
        
    return cnt