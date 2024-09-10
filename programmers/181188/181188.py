def solution(targets) :
    targets.sort(lambda x : x[1])
    
    min_b = targets[0][1] # 처음의 끝 값
    ea = 1
    for target in targets[1:] :
        a, b = target
        if min_b < a :
            min_b = b
            ea += 1
    return ea