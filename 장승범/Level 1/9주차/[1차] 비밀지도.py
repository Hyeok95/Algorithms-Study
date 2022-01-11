def decode(k):
    map = []
    
    for i in k:
        if i == 0:
            map.append(' ' * len(k))
            continue
        else:
            temp_value = i
            l = len(k) - 1
            temp_map = [' '] * len(k)
            while temp_value > 1:
                if temp_value % 2 == 1:
                    temp_map[l] = '#'
                    l -= 1
                    temp_value = temp_value // 2
                else:
                    l -= 1
                    temp_value = temp_value // 2

            temp_map[l] = '#'

            map.append(''.join(temp_map))
        
    return map


def solution(n, arr1, arr2):
    
    map1 = decode(arr1)
    map2 = decode(arr2)
    
    result = [''] * n
     
    for i in range(n):
        for j in range(n):
            if map1[i][j] == '#' or map2[i][j] == '#':
                result[i] += '#'
            else:
                result[i] += ' '
    
    return result