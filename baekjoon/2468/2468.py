# 데이터 받아오기
map_size= int(input())

# 아직 잠기지 않은 지역 리스트 정의
not_submerged= [[True for i in range(map_size)] for i in range(map_size)]
# 아직 잠기지 않은 지역들을 리스트로 만듬
not_submerge_list= []
for x in range(map_size) :
    for y in range(map_size) :
        not_submerge_list.append((x,y))

max_height= 2
lines= []
for _ in range(map_size) :
    line= list(map(int, input().split(" ")))
    lines.append(line)

# 지역 탐색 방향 정의
rcs= [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]


max_space= 0
# 높이 1부터 100까지 탐색
for h in range(0,101) :
    space = 0
    # 방문한 지역 저장
    visited= set()
    # 모든 지역 탐색시작
    new_not_submerge_list= []
    for land in not_submerge_list :
        r,c= land
        # 잠긴 지역들은 False로 바꿈
        if lines[r][c] <= h :
            not_submerged[r][c]= False
        # 잠기지 않은 지역들은 따로 보관
        else :
            new_not_submerge_list.append((r,c))
    # 지역 정산, 잠기지 않은 지역들에서 안전 영역 계산
    not_submerge_list= [*new_not_submerge_list]
    visited= set()
    space= 0
    for land in not_submerge_list :
        # 미방문 지역들만 탐색
        if land not in visited :
            targets= set()
            targets.add(land)
            while targets :
                target= targets.pop()
                visited.add(target)
                r, c=target
                for rc in rcs :
                    x, y= rc
                    if not(0<=r+x<map_size and 0<= c+y < map_size) :
                        continue
                    elif (r+x, c+y) in visited :
                        continue
                    if not_submerged[r+x][c+y]:
                        targets.add((r+x, c+y))
            space = space + 1
    max_space= space if space > max_space else max_space
    # 모든 지역이 잠긴 경우 중단
    if space == 0 :
        break
print(max_space)