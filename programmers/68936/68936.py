def solution(arr) :
    total = [0, 0]
    # 바로 압축 가능한 쿼드인지 판단
    length = len(arr)
    cnt = {0:0, 1:0}
    for line in arr :
        for num in line :
            cnt[num] +=1
    for key, value in cnt.items() :
        if value == length**2 :
            total[key] +=1
            return total
    
    
    def quad_split(arr) :
        length = len(arr)
        if length == 1 :
                total[arr[0][0]] += 1
        else :
            all_cnt = (length//2)**2
            area1, area2, area3, area4 = [], [], [], []
            areas = [area1, area2, area3, area4]
            area1_cnt, area2_cnt, area3_cnt, area4_cnt = {0:0, 1:0}, {0:0, 1:0}, {0:0, 1:0}, {0:0, 1:0}
            for idx, line in enumerate(arr) :
                # 0, 1, 2, 3
                if idx < length//2 :
                    area1.append(line[:length//2])
                    area2.append(line[length//2:])
                else :
                    area3.append(line[:length//2])
                    area4.append(line[length//2:])
                for col, num in enumerate(line) :
                    if idx < length //2:
                        if col < length//2 :
                            area1_cnt[num] +=1
                        else :
                            area2_cnt[num] +=1
                    else :
                        if col < length//2 :
                            area3_cnt[num] +=1
                        else :
                            area4_cnt[num] +=1
            for index, cnt in enumerate([area1_cnt, area2_cnt, area3_cnt, area4_cnt]) :
                for key, value in cnt.items() :
                    if value == all_cnt :
                        areas[index] = [[key]]
            for area in areas :
                quad_split(area)
    quad_split(arr)
    return total