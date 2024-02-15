def solution(polynomial):
    inputs = polynomial.replace('+', '')
    polynomial = inputs.split('  ')
    b, bx = 0, 0
    for pol in polynomial :
        # 변수 처리
        if 'x' in pol : 
            pol = pol.replace('x', '')
            if pol == '' :
                bx += 1
            else :
                bx += int(pol)
        # 상수 처리
        else : 
            b += int(pol)
    if b != 0 and bx != 0 :
        if bx != 1 :
            return f"{bx}x + {b}"
        else :
            return f"x + {b}"
    elif b == 0 and bx != 0 :
        if bx != 1 :
            return f"{bx}x"
        else :
            return 'x'
    elif b != 0 and bx == 0 :
        return f"{b}"