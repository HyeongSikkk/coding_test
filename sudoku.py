# https://www.acmicpc.net/problem/2580

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


class TestError(Exception) :
    pass

class Solutioner :
    def __init__(self, array) :
        self.array = array
        self.target_list = self.get_target_list()
        self.boxes = self.box_maker()
        self.bundle_boxes = self.bundle_maker()
    
    def get_target_list(self) :
        target_list = []
        for row_idx, line in enumerate(self.array) :
            for col_idx, ea in enumerate(line) :
                if ea == "0" :
                    target_list.append((row_idx, col_idx))
        return target_list
    
    def box_maker(self) :
        boxes = []
        for target in self.target_list :
            row, col = target
            box = Box(row=row,col=col)
            box.mining(self.array)
            boxes.append(box)
        return boxes
    
    
    def bundle_maker(self) :
        bundle_boxes = [Bundle_box(bundle, self.boxes) for bundle in range(1, 10)]
        return bundle_boxes
    

    def re_mining(self, row, col, bundle) :
        for box in self.boxes :
            if box.row == row or box.col == col or box.bundle == bundle :
                box.mining(self.array)
                
                
    def select_one_cases_box(self) :
        # 숫자 경우의 수가 하나인 박스들 탐색
        for idx, box in enumerate(self.boxes) :
            if len(box.cases) == 1 :
                self.target_list.remove((box.row, box.col))
                self.boxes.remove(box)
                # 배열에 값 변경
                self.array[box.row][box.col] = box.cases[0]
                self.re_mining(box.row, box.col, box.bundle)

            # 지역 객체 재정비
            self.bundle_boxes = self.bundle_maker()
            

    # 번들에서 가능한 경우 탐색 후, 하나인 경우를 발견하면 해당 값 부여
    def select_one_cases_box_in_bundle(self) :
        # 각 번들 꺼내기
        for bundle_box in self.bundle_boxes :
            
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
                        break
                
                # 빈도 수가 1인 값을 가진 박스에 해당 값 주입하기
                for one in one_cases :
                    for box in bundle_box.boxes :
                        if one in box.cases :
                            self.array[box.row][box.col] = one
                            self.target_list.remove((box.row, box.col))
                            self.boxes.remove(box)
                            self.re_mining(box.row, box.col, box.bundle)
                            break
        
                self.bundle_boxes = self.bundle_maker()
                
        
    def solve(self) :
        while len(self.target_list) != 0 :
            before_array = [row[:] for row in self.array]
            self.select_one_cases_box()
            self.select_one_cases_box_in_bundle()
            if before_array == self.array :
                if len(self.target_list) != 0 :
                    self.reducing()
                    self.solve()
                break
    
    
    def reducing(self, min = True) :
        repair_array = [row[:] for row in self.array]
        repair_target_list = [i for i in self.target_list]
        repair_boxes = [i for i in self.boxes]
        repair_bundle_boxes = [i for i in self.bundle_boxes]
        
        if min : # 처음 호출된 경우
            # 제일 적은 숫자 경우의 수를 가진 박스 추출
            select_box = self.find_box()
            good_numbers = [] # 틀리지 않았다 판단되는 경우를 담는 리스트
            bad_numbers = [] # 틀린 경우를 담는 리스트

            for num in select_box.cases :
                if len(self.target_list) == 0 :
                    break
                result = self.do_test(num, select_box) # {'result' : boolean, 'num' : str(int)}
                if result['result'] :
                    good_numbers.append(num)
                else :
                    bad_numbers.append(num)

            if len(good_numbers) == 1 :
                self.choice(good_numbers[0], select_box)

            elif len(good_numbers) == 0 :
                raise TestError('TestError, zero case')
            elif len(bad_numbers) >= 1 and len(good_numbers) != 0 : # 테스팅 결과가 유의미한 경우
                select_box.wrong_cases = bad_numbers
                self.re_mining(select_box.row, select_box.col, select_box.bundle)

            else : # 틀리지 않은 경우들이 없을경우 다른 박스로 테스트
                self.reducing(min = False)
                
        else : # 첫 호출에서 풀이가 불가능 했을 경우
            select_box = self.find_box(min = False)
            good_numbers = [] # 틀리지 않았다 판단되는 경우를 담는 리스트
            bad_numbers = [] # 틀린 경우를 담는 리스트

            for num in select_box.cases :
                if len(self.target_list) == 0 :
                    break
                result = self.do_test(num, select_box) # {'result' : boolean, 'num' : str(int)}
                if result['result'] :
                    good_numbers.append(num)
                else :
                    bad_numbers.append(num)

            if len(good_numbers) == 1 :
                self.choice(good_numbers[0], select_box)

            elif len(bad_numbers) >= 1 : # 테스팅 결과가 유의미한 경우
                select_box.wrong_cases = bad_numbers
                self.re_mining(select_box.row, select_box.col, select_box.bundle)

        
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
        # 테스트 전의 배열, 테스트 결과에 실패 시에 원상복구 할 목적
        repair_array = [row[:] for row in self.array]
        repair_target_list = [i for i in self.target_list]
        repair_boxes = [i for i in self.boxes]
        repair_bundle_boxes = [i for i in self.bundle_boxes]
        
        # 테스트 시작
        self.choice(num, select_box)
        try :
            self.solve()
            self.array = repair_array
            self.target_list = repair_target_list
            self.boxes = repair_boxes
            self.bundle_boxes = repair_bundle_boxes
            return {'result' : True, 'num' : num}
        except :
            self.array = repair_array
            self.target_list = repair_target_list
            self.boxes = repair_boxes
            self.bundle_boxes = repair_bundle_boxes
            return {'result' : False, 'num' : num}
        
    
    def choice(self, num, box) :
        self.array[box.row][box.col] = num
        self.target_list.remove((box.row, box.col))
        self.boxes.remove(box)
        self.re_mining(box.row, box.col, box.bundle)
        self.bundle_boxes = self.bundle_maker()
    
    def repair(self) :
        self.target_list = self.get_target_list()
        self.boxes = self.box_maker()
        self.bundle_boxes = self.bundle_maker()
        
    def do(self) :
        while len(self.target_list) != 0 :
            self.solve()
            self.repair()
        
    
        
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
        self.wrong_cases = []
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
        
        if len(target_numbers) == 0 :
            raise TestError(f'TestError, {row_idx, col_idx}')
        
        if len(self.wrong_cases) == 0 :
            self.cases = target_numbers
        else :
            for target in target_numbers :
                if target in self.wrong_cases :
                    target_numbers.remove(target)
            
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


s = Solutioner(array)

s.do()
text = ''
for line in s.array :
    text += ' '.join(line)+'\n'
print(text)