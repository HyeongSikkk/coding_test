# 데이터 받아오기
map_size= int(input())
lines= []
max_height= 2
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

# 잠기지 않은 지역 탐색, 현재 로직에선 쓰이지 않음
def find_space(row, col, h) :
    targets= [(row, col)]
    visited= set()
    while targets :
        target= targets.pop(0)
        visited.add(target)
        r, c= target
        for rc in rcs :
            x, y= rc
            
            if not(0<=r+x<map_size and 0<= c+y < map_size) :
                continue
            elif (r+x, c+y) in visited :
                continue
            
            if lines[r+x][c+y] > h :
                targets.append((r+x, c+y))
    return
max_space= 0
# 높이 1부터 100까지 탐색
for h in range(1,101) :
    space = 0
    # 방문한 지역 저장
    visited= set()
    # 모든 지역 탐색시작
    for row, line in enumerate(lines) :
        for col, ea in enumerate(line) :
            # 잠기지 않은 지역 발견 시 주변 지역 탐색 시작
            if ea > h and (row, col) not in visited:
                # 잠기지 않은 지역의 인근 지역들은 targets 변수에 담겨짐
                targets= [(row, col)]
                while targets :
                    target= targets.pop(0)
                    visited.add(target)
                    r, c= target
                    for rc in rcs :
                        x, y= rc
                        if not(0<=r+x<map_size and 0<= c+y < map_size) :
                            continue
                        elif (r+x, c+y) in visited :
                            continue
                        
                        if lines[r+x][c+y] > h :
                            targets.append((r+x, c+y))
                space = space + 1
    max_space= space if space > max_space else max_space
    # 모든 지역이 잠긴 경우 중단
    if space == 0 :
        break
print(max_space)