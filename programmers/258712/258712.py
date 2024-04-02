def solution(friends, gifts) :
    length = len(friends)

    to_gift = {friends[idx] : {who : 0 for who in [*friends[:idx], *friends[idx+1:]]} for idx in range(length)}
    result = {who : 0 for who in friends}

    # 이번달 선물 집계
    for gift in gifts :
        send, receive = gift.split(' ')
        to_gift[send][receive] += 1

    # 다음달 선물 처리
    for i in range(length-1) :
        for j in range(i+1, length) :
            a, b = friends[i], friends[j]
            a_cnt, b_cnt = to_gift[a][b], to_gift[b][a]

            # 두 대상자 간 선물횟수 비교
            if a_cnt > b_cnt :
                result[a] += 1
            elif b_cnt > a_cnt :
                result[b] += 1

            # 선물횟수가 같은 경우
            else :
                a_gift_cnt, b_gift_cnt = 0, 0
                for key, value in to_gift.items() :
                    if key != a :
                        a_gift_cnt += value[a]

                    if key != b :
                        b_gift_cnt += value[b]

                a_gift_point = sum(to_gift[a].values()) - a_gift_cnt
                b_gift_point = sum(to_gift[b].values()) - b_gift_cnt

                if a_gift_point > b_gift_point :
                    result[a] += 1
                elif b_gift_point > a_gift_point :
                    result[b] += 1

    return max(result.values())