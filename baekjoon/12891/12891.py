import sys
input= sys.stdin.readline

# 개수와 패스워드길이 입력받기
S, P= tuple(map(int, input().split(" ")))

# 임의의 문자열 입력받기
text= input()

# acgt 개수조건 입력받기
nums= list(map(int, input().split(" ")))
acgt= {
    "A": nums[0],
    "C": nums[1],
    "G": nums[2],
    "T": nums[3],
}

cur_acgt= {
    "A": 0,
    "C": 0,
    "G": 0,
    "T": 0,
}

answer= 0
i, j= 0, 0
cur_acgt[text[j]]+= 1
while j< S :
    if i+P-1> j :
        j+=1
        cur_acgt[text[j]]+= 1
    else :
        this_good= True
        for ea in acgt :
            if acgt[ea]> cur_acgt[ea] :
                this_good= False
                break
        if this_good :
            answer+= 1
        cur_acgt[text[i]]-= 1
        i+= 1
        if i+P > S:
            break
print(answer)