map_size = input().strip().split(' ')
position_status = input().strip()
r, c, d = list(map(int, position_status.split(' ')))

row_size, col_size = list(map(int, map_size))

room = []
for _ in range(row_size) :
    room.append(input().strip().split(' '))
cnt = 0
while True :
    if room[r][c] == '0' :
        room[r][c] = 'cleaned'
        cnt += 1
    
    not_find = True
    for fr, fc in zip([1, -1, 0, 0], [0, 0, 1, -1]) :
        if 0<= r+fr <= row_size-1 and 0 <= c + fc <= col_size-1 :
            if room[r+fr][c+fc] == '0' :
                not_find = False
                d -= 1
                if d < 0 :
                    d = 3
                
                if d == 0 :
                    if r-1 >= 0 :
                        if room[r-1][c] == '0' :
                            r -= 1
                elif d == 2 :
                    if row_size > r+1 :
                        if room[r+1][c] == '0' :
                            r += 1
                elif d == 1 :
                    if col_size > c+1 :
                        if room[r][c+1] == '0' :
                            c += 1
                else :
                    if c-1 > 0 :
                        if room[r][c-1] == '0' :
                            c -= 1
                break
                        
    if not_find :
        if d == 0 :
            if room[r+1][c] == '1' :
                break
            r += 1
        elif d == 1 :
            if room[r][c-1] == '1' :
                break
            c -= 1
        elif d == 2 :
            if room[r-1][c] == '1' :
                break
            r -= 1
        else : # d == 3
            if room[r][c+1] == '1' :
                break
            c += 1
print(cnt)