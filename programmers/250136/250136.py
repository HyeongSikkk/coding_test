def solution(land):
    searched = {}
    
    def calc(oils, r, c) :
        try :
            if land[r][c] == 1 and c >= 0 and r >= 0 :
                land[r][c] = 0
                if (r, c) not in oils :
                    oils.append((r, c))
                try :
                    searched[(r+1, c)]
                except :
                    calc(oils, r + 1, c)
                    searched[(r+1, c)] = True
                
                try :
                    searched[(r, c+1)]
                except :
                    calc(oils, r, c + 1)
                    searched[(r, c+1)] = True
                
                try :
                    searched[(r-1, c)]
                except :
                    calc(oils, r - 1, c)
                    searched[(r-1, c)] = True
                
                try :
                    searched[(r, c-1)]
                except :
                    calc(oils, r, c - 1)
                    searched[(r, c-1)] = True
           
        except :
            pass
    
    ## 동작되는 코드
    total = {a : 0 for a in range(len(land[0]))}
    for c in range(len(land[0])) :
        for r in range(len(land)) :
            try :
                searched[(r, c)]
            except :
                searched[(r, c)] = True
                if land[r][c] == 1 :
                    oils = []
                    calc(oils, r, c)
                    width = list(map(lambda x : x[1], oils))
                    width_list = [a for a in range(min(width), max(width)+1)]
                    ea = len(oils)
                    for c in width_list :
                        total[c] += ea
    return max(total.values())