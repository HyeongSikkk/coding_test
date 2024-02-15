def solution(r1, r2) :
    bar = 4*(r2 - r1 + 1)
    cnt = 0
    for i in range(1, r2) :
        if i < r1 :
            l2 = int((r2**2 - i**2)**0.5)
            l1 = (r1**2 - i**2)**0.5
            l1 = int(l1) + 1 if int(l1) < l1 else int(l1)
            cnt += l2-l1+1
        else :
            l2 = int((r2**2 - i**2)**0.5)
            cnt += l2
    return bar+4*cnt
