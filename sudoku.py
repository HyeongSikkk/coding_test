import sys

# 입력값 받기
inputs = sys.stdin.readline
a = inputs.split('\n')
array = list(map(lambda x : x.split(' '), a))

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
        self.all_cases = [str(i) for i in range(1, 10)]
    
    def solution(self) :
        if self.idx == len(self.target_list) :
            #return print(s.array)
            return 0
        target_position = self.target_list[self.idx]
        target_numbers_row = [str(i) for i in range(1, 10)] # 가로만 다룸
        target_numbers_col = [str(i) for i in range(1, 10)] # 세로만 다룸
        target_numbers = [] # 둘에서 겹치는 것만 병합
        # 가로줄 파싱
        for ea in self.array[target_position[0]] :
            if ea != '0':
                target_numbers_row.remove(ea)
        
        # 세로줄 파싱
        for line in self.array :
            if line[target_position[1]] != '0':
                target_numbers_col.remove(line[target_position[1]])
        
        # 가로줄과 세로줄에서 둘 다 있는 값만 저장
        for target in target_numbers_row :
            if target in target_numbers_col :
                target_numbers.append(target)
        
        if len(target_numbers) == 0 :
            #print(self.idx, target_numbers)
            #print('값이 없엉')
            return 0
        
        self.idx += 1
        for target in target_numbers :
            self.array[target_position[0]][target_position[1]] = target
            print(f"position {target_position}, value = {target}")
            self.solution()


s = Solutioner(array, target_list)

s.solution()
text = ''
for line in s.array :
    text += ' '.join(line)+'\n'
print(text)