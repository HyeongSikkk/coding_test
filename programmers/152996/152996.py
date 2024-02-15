def solution(weights) :
    to_dict = {}
    answer = 0
    for num in weights :
        if num in to_dict :
            answer += to_dict[num]
            to_dict[num] += 1
        else :
            to_dict[num] = 1

    sorted_list = sorted(to_dict.items(), key = lambda x : x[0])
    to_dict = {key : value for key, value in sorted_list}
    keys = list(to_dict.keys())
    for idx in range(len(keys)) :
        for idx2 in range(idx+1, len(keys)) :
            num1, num2 = keys[idx], keys[idx2]
            if num1 * 2 < num2 :
                break
            if num1 / num2 in [2/3, 2/4, 3/4] :
                answer += to_dict[num1]*to_dict[num2]
    return answer