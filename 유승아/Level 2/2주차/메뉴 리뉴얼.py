from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []
    
    for c in course :
        order_combi = []
        for order in orders:
            # 만들 수 있는 경우의 수 (course 개수에 맞는)
            for combi in combinations(order,c):
                order_combi.append(''.join(sorted(combi)))
        
        # 메뉴조합, 주문횟수 -> 주문횟수 많은 순서대로 
        order_count = Counter(order_combi).most_common()
        
        result += [ k for k, v in order_count if v > 1 and v == order_count[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]