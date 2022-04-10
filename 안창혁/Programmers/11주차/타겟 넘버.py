def solution(numbers, target):
    count = 0
    visited = [0]
    
    for num in numbers:
        temp = []
        for i in visited:
            temp.append(i + num)
            temp.append(i - num)
        visited = temp
        
    for i in visited:
        if i == target:
            count += 1
    
    return count