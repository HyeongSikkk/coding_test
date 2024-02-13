import sys

# 입력값 받기
input = sys.stdin.readline
array = {}
for i in range(9) :
    inputed = input().strip()
    input_dict = {idx : num for idx, num in enumerate(inputed.split(' '))}
    array[i] = input_dict

def get_target_list(array) :
    target_list = []
    for row, line in array.items() :
        for col, num in line.items() :
            if num == '0' :
                target_list.append((row, col))
    return target_list

def solution(target_list) :
    find = False
    for idx, position in enumerate(target_list) :
        row, col = position
        if array[row][col] == '0' :
            find = True
            break
    if not find : # 공백이 다 메워진 경우
        return
    
    numbers = get_numbers(row, col)
    if len(numbers) == 0 :
        return
    for num in numbers :
        array[row][col] = num
        solution(target_list)
        success = True
        for position in target_list :
            test_row, test_col = position
            if array[test_row][test_col] == '0' :
                success = False
        if success :
            break
    
    for position in target_list :
        test_row, test_col = position
        if array[test_row][test_col] == '0' :
            array[row][col] = '0'
            break

def get_numbers(row, col) :
    target_numbers_row = [str(i) for i in range(1, 10)] # 가로만 다룸
    target_numbers_col = [str(i) for i in range(1, 10)] # 세로만 다룸
    target_numbers_bundles = [str(i) for i in range(1, 10)] # 뭉치만 다룸
    target_numbers = [] # 둘에서 겹치는 것만 병합

    # 가로줄 파싱
    for ea in array[row].values() :
        if ea != '0':
            target_numbers_row.remove(ea)

    # 세로줄 파싱
    for line in array.values() :
        if line[col] != '0':
            target_numbers_col.remove(line[col])

    # 뭉치 인식
    if row <= 2 :
        row_positions = [i for i in range(3)] # [0, 1, 2]
    elif row <= 5 :
        row_positions = [i for i in range(3, 6)] # [3, 4, 5]
    elif row <= 8 :
        row_positions = [i for i in range(6, 9)] # [6, 7, 8]
        
    if col <= 2 :
        col_positions = [i for i in range(3)] # [0, 1, 2]
    elif col <= 5 :
        col_positions = [i for i in range(3, 6)] # [3, 4, 5]
    elif col <= 8 :
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
    return target_numbers

def print_array(array) :
    text = ""
    for line in array.values() :
        text += ' '.join(line.values())
        text += '\n'
    print(text)
    
target_list = get_target_list(array)
solution(target_list)
print_array(array)