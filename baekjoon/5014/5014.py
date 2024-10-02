F, S, G, U ,D= tuple(map(int, input().split(" ")))
# S -> G
visited= set()
i= 0 # floor 리스트의 인덱싱용도와 엘리베이터 버튼 누른 횟수
cur_floor= S
minf, maxf= 1, F
while True :
    if S == G :
        print(0)
        break
    upf, downf= cur_floor+U, cur_floor-D
    if upf > maxf and downf < minf :
        print("use the stairs")
        break
    
    elif upf > maxf :
        cur_floor= downf
        i = i +1
    elif downf < minf :
        cur_floor= upf
        i = i +1
    else :
        up, down= abs(G-upf), abs(G-downf)
        if up < down :
            cur_floor= upf
            i = i +1
        else :
            cur_floor= downf
            i = i + 1
    
    if cur_floor== G :
        print(i)
        break
    elif cur_floor not in visited :
        visited.add(cur_floor)
    else :
        print("use the stairs")
        break