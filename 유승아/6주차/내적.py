def solution(a, b):
    dot = 0
    for a, b in zip(a,b):
        dot += a * b
    
    return dot