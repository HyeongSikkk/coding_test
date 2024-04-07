m,n,h = list(map(int, input().strip().split(' ')))

targets = [[]]
tensor = []
for f in range(h) :
    floor = []
    for r in range(n) :
        tmp = input().split(' ')
        for c in range(len(tmp)) :
            if tmp[c] == '1' :
                targets[0].append((r, c, f))
        floor.append(tmp)
        
        
    tensor.append(floor)

day = -1
completed = True
fore_casts = [
    (0, 0, -1),
    (0, 0, 1),
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
]
while targets :
    day += 1
    target_list = targets.pop()
    new_target = []
    for target in target_list :
        r, c, t = target
        for cast in fore_casts :
            fr, fc, ft = cast
            if 0<= r+fr <n and 0<= c+fc <m and 0<= t+ft <h :
                if tensor[t+ft][r+fr][c+fc] == '0' :
                    tensor[t+ft][r+fr][c+fc] = '1'
                    new_target.append((r+fr, c+fc, t+ft))
    if len(new_target) != 0 :
        targets.append(new_target)

for t in tensor :
    for r in t :
        if '0' in r :
            completed = False
            break
if completed :
    print(day)
else :
    print(-1)
