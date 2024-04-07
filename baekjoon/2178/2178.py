rows, cols = map(int, input().strip().split(' '))
maps = []
target_list = []
camed = set()
for _ in range(rows) :
    maps.append(input().strip())
maps = list(map(list, maps))
fore_casts = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
    ]
n = 0
now = [(0, 0)]

# def map_print(now) :
    
#     for r_idx, row in enumerate(maps) :
#         text = ''
#         for c_idx, ea in enumerate(row) :
#             if (r_idx, c_idx) in now :
#                 text += 'F'
#             else :
#                 text += ea
#         print(text)
#     print()

camed.add(now[0])
while True :
    find = False
    n += 1
    now += target_list
    target_list = []
#    map_print(now)
    for position in now :
        r, c = position
        if r == rows-1 and c == cols -1 :
            find = True
            break
        for fore_cast in fore_casts :
            fr, fc = fore_cast
            if 0 <= r+fr < rows and 0 <= c+fc < cols and (r+fr, c+fc) not in camed:
                if maps[r+fr][c+fc] == '1' :
                    target_list.append((r+fr, c+fc))
                    camed.add((r+fr, c+fc))
    now = []
    if find :
        print(n)
        break