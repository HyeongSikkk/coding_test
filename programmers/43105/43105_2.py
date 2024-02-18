def solution(triangle) :
    length = len(triangle)
    def dfs(n) :
        if n == 0 :
            return dfs(n+1)
        elif n == length :
            return max(triangle[-1])
        else :
            for index in range(n+1) :
                if index == 0 : # 처음
                    triangle[n][index] += triangle[n-1][index]
                elif index == n : # 마지막
                    triangle[n][index] += triangle[n-1][index-1]
                else :
                    a, b = triangle[n-1][index-1], triangle[n-1][index]
                    c = a if a > b else b
                    triangle[n][index] += c
            return dfs(n+1)
    b = dfs(0)
    return b