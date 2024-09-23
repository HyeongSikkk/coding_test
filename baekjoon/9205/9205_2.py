test_case_length = int(input())
def check(x1, y1, x2, y2) :
    if abs(x1-x2)+abs(y1-y2) <= 1000 :
        return True
    else :
        return False
for _ in range(test_case_length) :
    
    # 편의점 갯수 받기
    store_cnt = int(input())
    
    # 집 위치
    home_x, home_y = tuple(map(int, input().strip().split(' ')))
    
    # 편의점 위치들 받기
    store_ways= {(home_x, home_y):[]} # {(x,y):[(x,y),...],...}
    
    for _ in range(store_cnt) :
        x, y = tuple(map(int, input().strip().split(' ')))
        temp= []
        for store in store_ways :
            sx, sy= store
            if check(x, y, sx, sy) :
                temp.append(store)
                store_ways[store].append((x,y))
        store_ways[(x,y)]=temp
        
    
    # # 편의점의 주변 편의점찾기
    # for key in store_ways :
    #     for target_key in store_ways :
    #         if key == target_key :
    #             continue
    #         else :
    #             x, y= key
    #             tx, ty= target_key
    #             if check(x, y, tx, ty) :
    #                 store_ways[key].append(target_key)
    #             else :
    #                 continue
        
    # 락 위치
    fes_x, fes_y = tuple(map(int, input().strip().split(' ')))
    
    # 집과 페스티벌 장소에 인근 편의점 있는지 탐색
    fes=[]
    for store in store_ways :
        x,y=store
        if check(x, y, fes_x, fes_y) :
            fes.append(store)
            store_ways[store].append((fes_x,fes_y))
        else :
            continue
    store_ways[(fes_x,fes_y)]=fes
    can_start, can_end= False, False
    if len(store_ways[(home_x,home_y)]) > 0 :
        can_start=True
    if len(store_ways[(fes_x,fes_y)]) > 0 :
        can_end=True
    
    # 집과 페스티벌 장소가 가까울 때
    if check(fes_x, fes_y, home_x, home_y) :
        print('happy')
    
    # 집에서 페스티벌 장소로 가기 위한 최소한의 편의점 갯수를 만족하지 않을 경우
    elif abs(fes_x - home_x)+abs(fes_y-home_y) % 1000 <= store_cnt :
        print('sad')
    
    # 시작 자체가 불가능한 경우
    elif not can_start and not can_end :
        print('sad')
        
    # 집과 페스티벌 장소가 멀 때
    else :
        finish= False
        went_stores= set()
        went_stores.add((home_x,home_y))
        def go_store(store) :
            x,y= store
            if check(x,y, fes_x, fes_y) :
                global finish
                finish= True
                return
            else :
                for next_store in store_ways[store] :
                    if next_store not in went_stores :
                        went_stores.add(next_store)
                        go_store(next_store)
                        if finish :
                            return
                        else :
                            went_stores.discard(next_store)
        go_store((home_x, home_y))
        if finish :
            print("happy")
        else :
            print("sad")