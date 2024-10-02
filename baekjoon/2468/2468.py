map_size= int(input())
lines= []
max_height= 2
for _ in range(map_size) :
    line= list(map(int, input().split(" ")))
    lines.append(line)

space= 0
rcs= [
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
]
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
for h in range(1,101) :
    space = 0
    visited= set()
    for row, line in enumerate(lines) :
        for col, ea in enumerate(line) :
            if ea > h and (row, col) not in visited:
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
    if space == 0 :
        break
print(max_space)