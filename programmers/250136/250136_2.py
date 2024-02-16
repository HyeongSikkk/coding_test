import sys

sys.setrecursionlimit(1000000) # 재귀횟수 때문에 에러발생함.

def solution(land) :
    cols = {i : 0 for i in range(len(land[0]))}
    class Gas :
        def __init__(self) :
            self.value = 0
            self.min_col = len(land[0])
            self.max_col = 0
        
        def add(self) :
            self.value += 1
        
        def record_col(self, col) :
            if self.min_col > col :
                self.min_col = col
            if self.max_col < col :
                self.max_col = col
        
        def report(self) :
            for col in range(self.min_col, self.max_col+1) :
                cols[col] += self.value
            
    def out_gas(row, col, g) :
        if row >= len(land) or col >= len(land[0]) or row < 0 or col < 0 :
            return
        if land[row][col] == 1 :
            land[row][col] = 0
            g.add()
            g.record_col(col)
            out_gas(row+1, col, g)
            out_gas(row-1, col, g)
            out_gas(row, col+1, g)
            out_gas(row, col-1, g)
        
        
    for row, line in enumerate(land) :
        for col, gas in enumerate(line) :
            if gas == 1 :
                g = Gas()
                out_gas(row, col, g)
                g.report()
    return max(cols.values())