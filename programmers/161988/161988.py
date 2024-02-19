def solution(sequence) :
    def calc(length, array) :
        results = []
        for start_idx in range(0, len(array) -length+1) :
            purse = array[start_idx:start_idx+length]
            plus, minus = 0, 0
            for idx,num in enumerate(purse) :
                plus += ((-1)**(idx))*num
                minus += ((-1)**(idx+1))*num
            results.append(plus if plus > minus else minus)
        value = max(results)
        return value


    n = len(sequence)
    max_value = 0
    for i in range(1, n+1) :
        value = calc(i, sequence) 
        if max_value < value :
            max_value = value
    return max_value