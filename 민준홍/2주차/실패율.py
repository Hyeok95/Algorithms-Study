def solution(N, stages):
    result = {}
    
    c = len(stages)
    for stage in range(1,N+1):
        if c != 0: # 이건 왜? 방어용 코딩??
            count = stages.count(stage)
            result[stage] = count/c
            c -= count
        else:
            result[stage] = 0
            
    return sorted(result, key=lambda x : result[x],
            reverse=True) #sorted key 정렬

# 딕셔너리
# d = dict()

#print('\n3. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1])')
# g = sorted(d.items(), key=lambda x: x[1])
# print(g)

# print('\n4. 딕셔너리 정렬 : sorted(d.items(), key=lambda x: x[1], reverse=True)')
# h = sorted(d.items(), key=lambda x: x[1], reverse=True)
# print(h)

# # 1. 딕셔너리 출력
# print("\n1. 기본 딕셔너리")
# print(d)

# # 딕셔너리 키 정렬 오름차순(디폴트)
# print("\n2. 키 정렬 sorted(d.items())")
# f = sorted(d.items())
# print(f)

# # 딕셔너리 키 정렬 내림차순
# print("\n3. 키 정렬 sorted(d.items(), reverse=True)")
# g = sorted(d.items(), reverse=True)
# print(g)

# # 딕셔너리 키만 정렬 및 출력1
# print("\n4. 키만 정렬 sorted(d.keys())")
# h = sorted(d.keys())
# print(h)

# # 딕셔너리 키만 정렬 및 출력2
# print("\n5. 키만 정렬 sorted(d)")
# i = sorted(d)
# print(i)
