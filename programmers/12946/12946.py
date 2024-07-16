def solution(n) :
    tower1 = [n-i for i in range(n)]
    tower = [
        tower1,
        [],
        [],
    ]
    
    # 기록 리스트
    log = []
    
    # 움직임 및 기록하는 함수
    def move(move_index: int, tower_index: int)-> None :
        tower[tower_index-1].append(tower[move_index-1].pop())
        log.append([move_index, tower_index])
        print(tower)
    
    # 동작들을 생성하는 함수
    def make_command(move_index:int, tower_index: int, number: int)-> list :
        other_index = 6 -move_index -tower_index
        one_two = [tower_index, other_index]
        
        target_tower = tower[move_index-1][-number:]
        make_command = []
        for idx, number in enumerate(target_tower):
            make_command.append((move_index, one_two[idx%2], number))
        return make_command[::-1]
    
    def do(n, target_index) :
        n_index = None
        for idx, t in enumerate(tower) :
            if n in t :
                n_index = idx
                break
        commands = make_command(n_index+1, target_index, n)
        for command in commands :
            a, b, num = command
            move(a, b)
            if num != 1 :
                do(num-1, b)
    do(n, 3)
    return log