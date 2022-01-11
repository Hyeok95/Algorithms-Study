def solution(sizes):
    sizes = [sorted(x) for x in sizes]
    A = sorted(sizes, key=lambda x:x[0], reverse=True)[0][0]
    B = sorted(sizes, key=lambda x:x[1], reverse=True)[0][1]
    return A * B