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
searched = set()
def dfs(n, cur) :
    if cur.value == b :
        print(n)
        exit()
    people = []
    if cur.parent is not None :
        people.append(cur.parent)
    people += cur.children
    roads = []
    for who in people :
        if who not in searched :
            roads.append(who)
            searched.add(who)
    for man in roads :
        dfs(n+1, man)
dfs(0, peoples[a])
print(-1)
        