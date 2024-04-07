lines = int(input())
towns = []
register = []
for _ in range(lines) :
    towns.append(list(input()))

def getter(row, col) :
    casts = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
    ]
    new_man = [(row, col)]
    for man in new_man :
        r, c = man
        for cast in casts :
            fr, fc = cast
            if 0 <= r+fr < len(towns) and 0 <= c+fc < len(towns[0]) :
                if towns[r+fr][c+fc] == '1' :
                    new_man.append((r+fr,c+fc))
                    towns[r+fr][c+fc] = '0'
    register.append(len(new_man))
    
    

for row in range(len(towns)) :
    for col in range(len(towns[0])) :
        if towns[row][col] == '1' :
            towns[row][col] = '0'
            getter(row, col)
register.sort()
print(len(register))
for a in register :
    print(a)