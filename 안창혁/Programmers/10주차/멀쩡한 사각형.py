import math
def solution(w,h):
    mul = w * h
    return mul -(w+h - math.gcd(w,h))

# 6-4 = 2

# 3 4
# 12-5=7

# 4 6
# 24-8 = 16

# 6 9
# 54-12 = 42