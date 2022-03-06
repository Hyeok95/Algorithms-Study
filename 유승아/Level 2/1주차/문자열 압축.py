def solution(s):
    answer = len(s)
    
    # 단어 한개씩 추가하며 슬라이싱
    for step in range(1, len(s) // 2 + 1):
        # 압축된 단어 저장
        compressed = ""
        prev = s[:step] # 처음부터 step만큼의 문자열 추출
        count = 1
        
        # 슬라이싱 단위만큼(step) 증가시키며, original 문자열과 비교
        for j in range(step, len(s), step):
            # original 문자열에 동일한 압축단어가 들어갈 때마다 압축 횟수(count) 증가
            if prev == s[j:j+step]:
                count += 1
            # 동일한 단어가 아닐 때,
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step] # 다시 초기화
                count = 1
        # 남아있는 문자열에 대해서 처리(동일한 압축단어가 계속 이어져서 처리가 안된 경우) 
        compressed += str(count) + prev if count >= 2 else prev
        
        # 기존 문자열보다 짧아지는 경우 answer값 가장 짧은 경우로 다시 저장
        answer = min(answer, len(compressed))
        
            
    return answer