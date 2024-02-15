# https://www.acmicpc.net/problem/9012

len_input = int(input())
strings = []
for _ in range(len_input) :
    string = input()
    strings.append(string)

for string in strings :
    while '()' in string :
        string = string.replace('()', '')
    if len(string) == 0 :
        print('YES')
    else :
        print('NO')