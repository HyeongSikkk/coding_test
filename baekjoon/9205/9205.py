test_case_length = int(input())
for _ in range(test_case_length) :
    
    # 편의점 갯수 받기
    store_cnt = int(input())
    
    # 집 위치
    home_x, home_y = tuple(map(int, input().strip().split(' ')))
    
    # 편의점 위치들 받기
    stores = []
    for _ in range(store_cnt) :
        x, y = tuple(map(int, input().strip().split(' ')))
        stores.append((x,y))
        
    # 락 위치
    fes_x, fes_y = tuple(map(int, input().strip().split(' ')))
    
    # 집과 페스티벌 장소에 인근 편의점 있는지 탐색
    can_start, can_end = False, False
    for store in stores :
        x, y = store
        if abs(home_x - x) + abs(home_y - y) <= 1000 :
            can_start = True
        if abs(fes_x - x) + abs(fes_y - y) <= 1000 :
            can_end = True
    
    # 성공 여부
    finish = False
    # 락 위치로 dfs 정의
    def dfs(x, y, store_list) :
        global finish
        if abs(fes_x-x)+abs(fes_y-y) <= 1000 :
            finish = True
            return
        for idx, store in enumerate(store_list) :
            tar_x, tar_y = store
            if abs(tar_x-x)+abs(tar_y-y) <= 1000 :
                dfs(tar_x, tar_y, [*store_list[:idx], *store_list[idx+1:]])
            if finish :
                return
                
    
    # 집과 페스티벌 장소가 가까울 때
    if abs(fes_x - home_x)+abs(fes_y-home_y) <= 1000 :
        print('happy')
    
    # 집에서 페스티벌 장소로 가기 위한 최소한의 편의점 갯수를 만족하지 않을 경우
    elif abs(fes_x - home_x)+abs(fes_y-home_y) % 1000 <= store_cnt :
        print('sad')
    
    # 시작 자체가 불가능한 경우
    elif not can_start and not can_end :
        print('sad')
        
    # 집과 페스티벌 장소가 멀 때
    else :
        for idx, store in enumerate(stores) :
            tar_x, tar_y = store
            if abs(home_x-tar_x)+abs(home_y-tar_y) <= 1000 :
                dfs(tar_x, tar_y, [*stores[:idx], *stores[idx+1:]])
            
            if finish :
                break
        if finish :
            print('happy')
        else :
            print('sad')