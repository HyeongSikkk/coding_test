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
    
    # 락 위치로 dfs 정의
    def dfs(x, y, store_list) :
        if abs(fes_x-x)+abs(fes_y-y) <= 1000 :
            return True
        for idx, store in enumerate(store_list) :
            tar_x, tar_y = store
            if abs(tar_x-x)+abs(tar_y-y) <= 1000 :
                return dfs(tar_x, tar_y, [*store_list[:idx], *store_list[idx+1:]])
        return False
    
    # 집과 페스티벌 장소가 가까울 때
    if abs(fes_x - home_x)+abs(fes_y-home_y) <= 1000 :
        print('happy')
        
    # 집과 페스티벌 장소가 멀 때
    else :
        can = False
        for idx, store in enumerate(stores) :
            tar_x, tar_y = store
            if abs(home_x-tar_x)+abs(home_y-tar_y) <= 1000 :
                if dfs(tar_x, tar_y, [*stores[:idx], *stores[idx+1:]]) :
                    can = True
                    break
        if can :
            print('happy')
        else :
            print('sad')