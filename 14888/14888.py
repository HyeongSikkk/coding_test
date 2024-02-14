funcs = []

N = int(input())
numbers = input().strip().split(' ')
operator = input().strip().split(' ')
# 문자열을 숫자로
operator_cnt = list(map(int, operator)) # ['0', '0', '1', '0'] -> [0, 0, 1, 0]

def operator_maker(operator) :
    oper = []
    for idx, num in enumerate(operator) :
        for _ in range(num) :
            if idx == 0 :
                oper.append('+')
            elif idx == 1 :
                oper.append('-')
            elif idx == 2 :
                oper.append('*')
            else :
                oper.append('//')
    return oper

def condition(func) :
    oper_cnt = {
        '+' : 0,
        '-' : 0,
        '*' : 0,
        '//' : 0
    }
    for oper in func[1::2] : # 연산자들만 oper변수에 지정
        oper_cnt[oper] += 1
    
    for inputed, now_cnt in zip(operator_cnt, oper_cnt.values()) :
        if inputed < now_cnt : # 주어진 갯수보다 많은 경우 
            return False
    return True
        

def solution(n, func) :
    if n == N :
        funcs.append(func)
            
    else :
        for oper in ['+', '-', '*', '//'] :
            if condition([*func, oper]) :
                solution(n+1, [*func, oper, numbers[n]])

operator = operator_maker(operator_cnt)
solution(1, [numbers[0]])

# 최대와 최소
max_value = int(-1e9)
min_value = -max_value

for func in funcs :
    a = func.pop(0)
    while len(func) != 0 :
        oper = func.pop(0)
        num = func.pop(0)
        if oper == '//' and int(a) < 0 :
            a = -eval(str(-a)+oper+num)
        else :
            a = eval(str(a)+oper+num)
    if max_value < a :
        max_value = a
    if min_value > a :
        min_value = a

print(max_value)
print(min_value)