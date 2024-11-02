import sys

# 데이터 입력받아오기, # 3<= N <= 300, 3<= M <= 300
N, M= tuple(map(int, sys.stdin.readline().split(" ")))
ice_mountains=[]
melted= [[False for i in range(M)] for i in range(N)]
not_melt_list= []
for i in range(N) :
    ice_mountains.append(list(map(int, input().split(" "))))   
    for idx, ea in enumerate(ice_mountains[i]) :
        if ea ==0 :
            melted[i][idx]= True
        else :
            not_melt_list.append((i, idx))
# 상하좌우 정의
rcs= [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
time=0
while len(not_melt_list) != 0 :
    checked= set()
    ice_mountain= 0
    melt_calc_list=[] # 빙산의 덩어리 수를 구하며, 녹을 빙산의 값도 미리 계산함
    for mountain in not_melt_list :
        if mountain not in checked :
            mountains= set()
            mountains.add(mountain)
            while mountains :
                m= mountains.pop()
                checked.add(m)
                x, y= m
                ea= 0
                for rc in rcs :
                    r,c= rc
                    next_x, next_y= x+r, y+c
                    if 0<= next_x < N and 0<= next_y < M :
                        if (next_x, next_y) not in checked and not melted[next_x][next_y]:
                            mountains.add((next_x, next_y))
                        elif melted[next_x][next_y] :
                            ea=ea+1
                melt_calc_list.append([x,y,ea])
            ice_mountain=ice_mountain+1
        else :
            continue
        
    if ice_mountain >= 2 :
        print(time)
        break
    # 빙산의 녹음 구현
    new_not_melt_list= []
    for melt in melt_calc_list :
        x, y, ea= melt
        ice_mountains[x][y]= ice_mountains[x][y]-ea if ice_mountains[x][y]-ea > 0 else 0
        if ice_mountains[x][y] == 0 :
            melted[x][y]= True
        else :
            new_not_melt_list.append((x,y))
    time = time + 1
    if len(new_not_melt_list) == 0 :
        print(0)
        break
    not_melt_list= new_not_melt_list