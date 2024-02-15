# https://www.acmicpc.net/problem/14889

humans = int(input())
combi_array = {}
for index in range(humans) :
    combi = input().split(' ') # "a b ... Z"를 입력받아서 ["a", "b", ..., "z"]
    combi_array[index] = {index : int(num) for index, num in enumerate(combi)}

results = []

def calc(team, another_team) :
    team_value, another_team_value = 0, 0
    # 팀 밸류 계산
    for i in team :
        for j in team :
            if i == j :
                continue
            team_value += combi_array[i][j]
    
    # 어나더 팀 밸류 계산
    for i in another_team :
        for j in another_team :
            if i == j :
                continue
            another_team_value += combi_array[i][j]
    
    return team_value - another_team_value if team_value >= another_team_value else -team_value + another_team_value
    
    
def solution(team = []) :
    if len(team) == humans//2 : # 팀이 다 결성된 경우
        another_team = []
        for who in range(humans) :
            if who in team :
                continue
            another_team.append(who)
        result = calc(team, another_team)
        results.append(result)
    else :
        if len(team) == 0 :
            range_ = range(humans)
        else :
            range_ = range(team[-1]+1, humans)
        for who in range_ :
            if not who in team :
                solution([*team, who])
    

solution()
print(min(results))