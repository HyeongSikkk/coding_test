# https://www.acmicpc.net/problem/9663
import time

len_queens = int(input())
start = time.time()
cnt = [0]
def board_maker(n) :
    return {idx:{idx:0 for idx in range(n)} for idx in range(n)}

def check(row, col, n = len_queens) :
    #for num in board.values() :
    #    if num[col] == 1 :
    #        return False
    
    # y = x 방향 
    # col을 0으로 만들고 시작
    s_row, s_col = row, col
    for _ in range(col) :
        if s_row == n - 1 :
            break
        s_col -= 1
        s_row += 1
    # y=x 방향으로 탐색 시작
    while True :
        try :
            if board[s_row][s_col] == 1 :
                return False
        except :
            break
        s_row -= 1
        s_col += 1
        
    # y = -x 방향
    # row를 0으로 만들고 시작
    s_row, s_col = row, col
    for _ in range(col) :
        if s_row == 0 :
            break
        s_col -= 1
        s_row -= 1
    while True :
        try :
            if board[s_row][s_col] == 1 :
                return False
        except :
            break
        s_row += 1
        s_col += 1
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