def solution(triangle) :
    length = len(triangle)
    result = [0]
    def dfs(n, index, value) :
        if n == length :
            if result[0] < value :
                result[0] = value
        else :
            value += triangle[n][index]
            dfs(n+1, index, value)
            dfs(n+1, index+1, value)
    dfs(0, 0, 0)
    return result[0]