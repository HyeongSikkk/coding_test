# https://www.acmicpc.net/problem/9663
import time

len_queens = int(input())
start = time.time()
cnt = [0]
def board_maker(n) :
    return [[0 for i in range(n)]for i in range(n)]

def print_array(array) :
    text = ''
    for line in array :
        line_ = list(map(str, line))
        text += ' '.join(line_)+'\n'
    print(text)

def check(row, col, n = len_queens) :
    # y = x 방향 
    # col을 0으로 만들고 시작
    s_row, s_col = row, col
    # 2, 3 -> 2, 3
    # 
    if row+col < len_queens :
        value = col
        s_row += value
        s_col -= value
    else :
        value = n -1 -row
        s_row += value
        s_col -= value
    for i in range(n) :
        if s_row < 0 or s_col == n :
            break
        if board[s_row][s_col] == 1 :
            return False
        s_row -= 1
        s_col += 1
    # y = -x 방향
    # row를 0으로 만들고 시작
    s_row, s_col = row, col
    value = len_queens -1 - s_row if s_row > s_col else len_queens -1 -s_col
    s_row += value
    s_col += value
    for i in range(s_row + 1 if s_row < s_col else s_col + 1) :
        if board[s_row][s_col] == 1 :
            return False
        s_row -= 1
        s_col -= 1
    return True
        
def solution(n, cols = [i for i in range(len_queens)]) :
    if n == len_queens :
        cnt[0] += 1
    else :
        for index, col in enumerate(cols) :
            if check(n, col) :
                board[n][col] = 1
                solution(n+1, [*cols[:index], *cols[index+1:]])
                board[n][col] = 0

board = board_maker(len_queens)
solution(0)
end = time.time()
print(cnt[0])
print(f"elapsed time : {round(end - start, 2)}")