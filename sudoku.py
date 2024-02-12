import sys

# 입력값 받기
input = sys.stdin.readline
array = []
for _ in range(9) :
    inputed = input().strip()
    array.append(inputed.split(' '))


# "0"값들 파싱
target_list = []
for row_idx, line in enumerate(array) :
    for col_idx, ea in enumerate(line) :
        if ea == "0" :
            target_list.append((row_idx, col_idx))


class Solutioner :
    def __init__(self, array, target_list) :
        self.array = array
        self.target_list = target_list
        self.idx = 0
        self.boxes = self.box_maker()
        self.bundel_boxes = self.bundle_maker()
    
    def box_maker(self) :
        boxes = []
        for target in self.target_list :
            row, col = target
            box = Box(row=row,col=col)
            box.mining(self.array)
            boxes.append(box)
        
        for idx, box in enumerate(boxes) :
            # 첫 박스
            if idx == 0 :
                box.backward = boxes[idx+1]
            
            # 마지막 박스
            elif idx == len(boxes)-1 :
                box.forward = boxes[idx-1]
            
            # 그 외 박스
            else :
                box.forward = boxes[idx-1]
                box.backward = boxes[idx +1]
        return boxes
    
    
    def bundle_maker(self) :
        bundle_boxes = []
        
        for bundle in range(1, 10) : # 1, 2, 3, ... , 9
            bundle_boxes.append(Bundle_box(bundle, self.boxes))
        
        return bundle_boxes
    
    
    def re_bundle_maker(self) :
        bundle_boxes = []
        
        for bundle in range(1, 10) : # 1, 2, 3, ..., 9
            bundle_boxes.append(Bundle_box(bundle, self.boxes))
        
        self.bundel_boxes = bundle_boxes
        
        
    def re_mining(self, row, col, bundle) :
        for box in self.boxes :
            if box.row == row or box.col == col or box.bundle == bundle :
                box.mining(self.array)
                
    def select_one_cases_box(self, re = True) :
        # 숫자 경우의 수가 하나인 박스들 탐색
        good_box = []
        for idx, box in enumerate(self.boxes) :
            if len(box.cases) == 1 :
                good_box.append(box)
                if re :
                    self.target_list.remove((box.row, box.col))
                    self.boxes.remove(box)
        
        if len(good_box) != 0 :
            # 배열에 값 변경
            for box in good_box :
                self.array[box.row][box.col] = box.cases[0]
                self.re_mining(box.row, box.col, box.bundle)
                
            # 지역 객체 재정비
            if re :
                self.re_bundle_maker()
            

    # 번들에서 가능한 경우 탐색 후, 하나인 경우를 발견하면 해당 값 부여
    def select_one_cases_box_in_bundle(self, re = True) :
        # 각 번들 꺼내기
        for bundle_box in self.bundel_boxes :
            
            # 번들에서 박스들 꺼내서 한 값만 가능한 경우 탐색
            numbers = {}
            for box in bundle_box.boxes :
                
                # 각 경우의 빈도 수 구하기
                for num in box.cases :
                    if num in numbers :
                        numbers[num] += 1
                    else :
                        numbers[num] = 1
            
            # 빈도 수 중에 1이 있는지 탐색
            if 1 in numbers.values() :
                
                one_cases = []
                # 빈도 수가 1인 값 찾기
                for key, value in numbers.items() :
                    if value == 1 :
                        one_cases.append(key)
                
                # 빈도 수가 1인 값을 가진 박스에 해당 값 주입하기
                for one in one_cases :
                    for box in bundle_box.boxes :
                        if one in box.cases :
                            self.array[box.row][box.col] = one
                            self.target_list.remove((box.row, box.col))
                            self.boxes.remove(box)
                            self.re_mining(box.row, box.col, box.bundle)
        
        if re :
            self.re_bundle_maker()
                
                    
        
    def solve(self) :
        while True :
            before_array = [row[:] for row in self.array]
            self.select_one_cases_box()
            self.select_one_cases_box_in_bundle()
            if before_array == self.array :
                if len(target_list) != 0 :
                    self.reducing()
                break
        
        
    
    
    def reducing(self) :
        # 제일 적은 숫자 경우의 수를 가진 박스 추출
        select_box = self.find_box()
        good_numbers = [] # 틀리지 않았다 판단되는 경우를 담는 리스트
        
        for num in select_box.cases :
            if len(self.target_list) == 0 :
                break
            result = self.do_test(num, select_box) # {'result' : boolean, 'num' : str(int)}
            if result['result'] :
                good_numbers.append(num)
        
        if len(good_numbers) == 1 :
            if len(self.target_list) != 0 :
                self.choice(good_numbers[0], select_box)
                self.solve()
        else :
            if len(self.target_list) != 0 :
                select_box = self.find_box(min = False)
                good_numbers = []
                for num in select_box.cases :
                    if len(self.target_list) == 0 :
                        break
                    result = self.do_test(num, select_box) # {'result' : boolean, 'num' : str(int)}
                    if result['result'] :
                        good_numbers.append(num)

                if len(good_numbers) == 1 :
                    if len(self.target_list) != 0 :
                        self.choice(good_numbers[0], select_box)
                        self.solve()

        
    # 제일 적은 숫자 경우의 수를 가진 박스 탐색
    def find_box(self, min = True) :
        if min :
            len_cases = 9
            select_box = None
            for box in self.boxes :
                if len(box.cases) < len_cases :
                    len_cases = len(box.cases)
                    select_box = box
            return select_box
        else :
            len_cases = 0
            select_box = None
            for box in self.boxes :
                if len(box.cases) > len_cases :
                    len_cases = len(box.cases)
                    select_box = box
            return select_box
    
    # 박스에 가능한 경우의 값을 넣어보기
    def do_test(self, num, select_box) :
        print(f"testing\n    {select_box.row, select_box.col} : {num}")
        # 테스트 전의 배열, 테스트 결과에 실패 시에 원상복구 할 목적
        repair_array = [row[:] for row in self.array]
        repair_target_list = [i for i in self.target_list]
        repair_boxes = [i for i in self.boxes]
        
        # 테스트 시작
        self.choice(num, select_box)
        try :
            self.solve()
            self.array = repair_array
            self.target_list = repair_target_list
            self.boxes = repair_boxes
            return {'result' : True, 'num' : num}
        except :
            self.array = repair_array
            self.target_list = repair_target_list
            self.boxes = repair_boxes
            return {'result' : False, 'num' : num}
        
    
    def choice(self, num, box) :
        print(f"choice\n    {box.row, box.col} : {num}")
        self.array[box.row][box.col] = num
        self.target_list.remove((box.row, box.col))
        self.boxes.remove(box)
        self.re_mining(box.row, box.col, box.bundle)
        self.re_bundle_maker()
        
    
        
class Bundle_box :
    def __init__(self, bundle, boxes) :
        self.bundle = bundle
        self.boxes = self.find_box(boxes)
    
    def find_box(self, boxes) :
        my_box = []
        for box in boxes :
            if box.bundle == self.bundle :
                my_box.append(box)
        return my_box
           
class Box :
    def __init__(self, row, col) :
        self.row = row
        self.col = col
        self.bundle = get_bundle(row, col)
    
    def mining(self, array) :
        target_numbers_row = [str(i) for i in range(1, 10)] # 가로만 다룸
        target_numbers_col = [str(i) for i in range(1, 10)] # 세로만 다룸
        target_numbers_bundles = [str(i) for i in range(1, 10)] # 뭉치만 다룸
        target_numbers = [] # 둘에서 겹치는 것만 병합
        row_idx = self.row
        col_idx = self.col
        
        # 현재 값이 "0"이 아닌 경우
        if array[row_idx][col_idx] != "0" :
            array[row_idx][col_idx] = "0"
        # 가로줄 파싱
        for ea in array[row_idx] :
            if ea != '0':
                target_numbers_row.remove(ea)
        
        # 세로줄 파싱
        for line in array :
            if line[col_idx] != '0':
                target_numbers_col.remove(line[col_idx])
                       
        # 뭉치 인식
        if row_idx <= 2 :
            row_positions = [i for i in range(3)] # [0, 1, 2]
        elif row_idx <= 5 :
            row_positions = [i for i in range(3, 6)] # [3, 4, 5]
        elif row_idx <= 8 :
            row_positions = [i for i in range(6, 9)] # [6, 7, 8]
        
        if col_idx <= 2 :
            col_positions = [i for i in range(3)] # [0, 1, 2]
        elif col_idx <= 5 :
            col_positions = [i for i in range(3, 6)] # [3, 4, 5]
        elif col_idx <= 8 :
            col_positions = [i for i in range(6, 9)] # [6, 7, 8]
        
        # 뭉치 파싱
        for bundle_row in row_positions :
            for bundle_col in col_positions :
                if array[bundle_row][bundle_col] != "0" :
                    target_numbers_bundles.remove(array[bundle_row][bundle_col])
                    
        # 가로줄, 세로줄, 뭉치에서 공통적으로 존재하는 값만 저장
        for target in [*target_numbers_row, *target_numbers_col, *target_numbers_bundles] :
            if target in target_numbers_row and target in target_numbers_col and target in target_numbers_bundles :
                if target not in target_numbers :
                    target_numbers.append(target)
        
        self.cases = target_numbers

def get_bundle(row_idx, col_idx) :
    if row_idx <= 2 :
        row_positions = 1
    elif row_idx <= 5 :
        row_positions = 2
    elif row_idx <= 8 :
        row_positions = 3
    
    if col_idx <= 2 :
        col_positions = 0
    elif col_idx <= 5 :
        col_positions = 1
    elif col_idx <= 8 :
        col_positions = 2
    
    return row_positions+3*col_positions


s = Solutioner(array, target_list)

s.solve()
def check(array) :
    # 가로, 세로 테스트
    for row_idx in range(9) :
        for col_idx in range(9) :
            rows = []
            cols = []
            
            for row in array[row_idx] :
                if not row in rows :
                    rows.append(row)
                else :
                    print('error')
                    print(row_idx, col_idx)
                    return

            for col in array :
                if not col[col_idx] in cols :
                    cols.append(col[col_idx])
                else :
                    print('error')
                    print(row_idx, col_idx)
                    return
                
    # bundel test
    row_bundles = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    col_bundles = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for rows in row_bundles :
        for cols in col_bundles :
            numbers = []
            for row in rows :
                for col in cols :
                    num = array[row][col]
                    if not num in numbers :
                        numbers.append(num)
                    else :
                        print('error')
                        return
    return 'perfect'



print(check(s.array))
text = ''
for line in s.array :
    text += ' '.join(line)+'\n'
print(text)