rows, cols = list(map(int, input().strip().split(' ')))
maps = []
for _ in range(rows) :
    maps.append(input().strip())
maps = list(map(list, maps))
def solver(n, position) :
    r, c = position
    if r == rows-1 and c == cols-1 :
        print(n)
        exit()
    maps[r][c] = '0'
    fore_casts = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]
    for fore_cast in fore_casts :
        fr, fc = fore_cast
        if 0 <= r+fr < rows and 0 <= c + fc < cols :
            if maps[r+fr][c+fc] == '1' :
                solver(n+1, (r+fr, c+fc))
solver(1, (0, 0))