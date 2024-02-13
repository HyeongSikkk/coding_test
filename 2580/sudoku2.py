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

target_list = get_target_list(array)

def condition(row, col, num) : 
    for row_num in array[row].values() :
        if num == row_num :
            return False
    
    for cols in array.values() :
        if num == cols[col] :
            return False
    
    for row_idx in range(3) :
        for col_idx in range(3) :
            if num == array[row//3 * 3 + row_idx][col//3 * 3 + col_idx] :
                return False
    
    return True

def print_array(array) :
    text = ""
    for line in array.values() :
        text += ' '.join(line.values())
        text += '\n'
    print(text)

def dfs(n) :
    if n == len(target_list) :
        print_array(array)
        exit()
        
    row, col = target_list[n]
    
    for num in range(1, 10) : # 1, 2, 3, ..., 9
        num = str(num)
        if condition(row, col, num) :
            array[row][col] = num
            dfs(n+1)
            array[row][col] = '0'
            
dfs(0)