def solution(n):
    string = str(n)
    return [int(string[x]) for x in range(len(string)-1, -1, -1)]