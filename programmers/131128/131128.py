def solution(x, y) :
    x_dict, y_dict = {}, {}
    for num in ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'] :
        before_x = len(x)
        x = x.replace(num, '')
        after_x = len(x)

        before_y = len(y)
        y = y.replace(num, '')
        after_y = len(y)
        x_dict[num] = before_x - after_x
        y_dict[num] = before_y - after_y
        
    union = ''
    for key, value in sorted(x_dict.items(), reverse = True) :
        if key in y_dict :
            if value <= y_dict[key] :
                union += f'{key}'*value
            elif value > y_dict[key] :
                union += f'{key}'*y_dict[key]
    if len(union) == 0 :
        return '-1'
    else :
        if union[0] == '0' :
            return '0'
        else :
            return union