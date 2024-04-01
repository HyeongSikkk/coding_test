class Node :
    def __init__(self,value) :
        self.value = value
        self.parent = None
        self.children = []

len_people = int(input().strip())
a, b = input().strip().split(' ')
cnt = int(input().strip())
peoples= {}
for _ in range(cnt) :
    par, child = input().strip().split(' ')
    if par not in peoples :
        peoples[par] = Node(par)
    par_node = peoples[par]
    if child not in peoples :
        peoples[child] = Node(child)
    child_node = peoples[child]
    par_node.children.append(child_node)
    child_node.parent = par_node
def dfs(n = 0, cur = None) :
    if n == 0 :
        cur = peoples[a]
    if cur.value == b :
        print(n)
        exit()
    roads = [cur.parent, *cur.children]
    for man in roads :
        dfs(n+1, man)
dfs()