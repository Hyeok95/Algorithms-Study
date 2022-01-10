# 내 풀이
def solution(n, lost, reserve):
    answer = int(n)-len(lost)
    answer2 = 0
    for i in range(len(lost)):
        if lost[i]+1 or lost[i]-1 in reserve:
            answer2 += 1
    answer = answer + answer2

    return answer  # 50점

# 베스트 코딩


def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)
