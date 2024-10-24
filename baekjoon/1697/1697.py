# 수빈이와 동생의 위치 받아오기
a, b= tuple(map(int, input().split(" ")))
passed=[False for i in range(int(1e+5)+1)]
# case1 수빈이가 무조건 뒤로 걸어가야 할 경우
if a > b :
    print(a- b)

else :
    # 너비우선탐색으로 동생의 위치로 나아가기
    nodes=[a]
    second=0 # 수빈이가 동생을 찾기까지 걸린 시간을 구하기
    while True :
        new_node= set()
        for node in nodes :
            passed[node]=True
            x1, x2, x3= node-1, node+1, node*2
            if not passed[x1] :
                new_node.add(x1)
            if x2<= 1e+5 :
                if not passed[x2] :
                    new_node.add(x2)
            if x3 <= 1e+5 :
                if not passed[x3] :
                    new_node.add(x3)
        second=second+1
        if b in new_node :
            print(second)
            break
        else :
            nodes=new_node