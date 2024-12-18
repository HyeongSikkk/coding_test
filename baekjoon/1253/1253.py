import sys
#input= sys.stdin.readline

# 데이터 갯수를 입력 받는다.
N= int(input())

# 데이터를 입력 받는다.
numbers= list(map(int, input().split(" ")))

# 데이터를 정렬한다.
numbers.sort()

# 투 포인터로 "좋은 수" 인지 판별한다.
answer= 0
for k in range(N) :
    num= numbers[k]
    i= 0
    j= N-1
    while i < j :
        cur= numbers[i]+ numbers[j]
        # k와 같은 인덱스 일 경우 스킵
        if i== k or j == k :
            if i == k :
                i+= 1
            else :
                j-= 1
        # "좋은 수"인 경우
        elif num== cur :
            answer+= 1
            break
        # cur가 작은 경우
        elif cur < num :
            i+= 1
        # cur가 큰 경우
        elif cur > num :
            j-= 1
print(answer)