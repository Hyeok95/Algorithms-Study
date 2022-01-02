def solution(arr1, arr2):
    
    result = []
    
    for i in range(len(arr1)):
        trial = []
        for j in range(len(arr1[i])):
            trial.append(arr1[i][j] + arr2[i][j])
        
        result.append(trial)
            
    
    return result