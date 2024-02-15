def solution(park, routes) :
    # get_position
    find = False
    for row, way in enumerate(park) :
        for col, w in enumerate(way) :
            if w == 'S' :
                find = True
                break
        if find :
            break

    for route in routes :
        where, length = route.split(' ')
        length = int(length)
        # 남
        if where == 'S' :
            if row + length >= len(park) :
                continue
            not_access = True
            for forward in range(length) :
                if park[row+forward+1][col] == 'X' :
                    not_access = False
            if not_access :
                row += length

        # 북
        elif where == 'N' :
            if row - length < 0 :
                continue
            not_access = True
            for forward in range(length) :
                if park[row-forward-1][col] == 'X' :
                    not_access = False
            if not_access :
                row -= length

        # 동
        elif where == 'E' :
            if col + length >= len(park[0]) :
                continue
            not_access = True
            for forward in range(length) :
                if park[row][col+forward+1] == 'X' :
                    not_access = False
            if not_access :
                col += length

        # 북
        elif where == 'W' :
            if col - length < 0 :
                continue
            not_access = True
            for forward in range(length) :
                if park[row][col-forward-1] == 'X' :
                    not_access = False
            if not_access :
                col -= length
    return [row, col]