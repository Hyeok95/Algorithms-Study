def solution(sizes):
    w_ = []
    h_ = []
    
    for w, h in sizes:
        # 회전시킬지 말지 결정 -> w <= h 경우 회전 시킨다.
        if w >= h:
            w_.append(w)
            h_.append(h)
        else:  
            h_.append(w)
            w_.append(h)

    return max(w_) * max(h_)