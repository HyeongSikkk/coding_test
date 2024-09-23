class Node :
    def __init__(self, value) :
        self.value = value
        self.wire= []
        self.detected= False
    
    def __repr__(self) :
        return str(self.value)
    
    def reset(self) :
        self.detected= False
    
    def sort(self) :
        self.wire.sort(key= lambda x : x.value)
        
len_node, len_wire, start= tuple(map(lambda x : int(x), input().split(" ")))
nodes= [0]+[Node(i) for i in range(1, len_node+1)]
for _ in range(len_wire) :
    a, b= tuple(map(lambda x : int(x), input().split(" ")))
    nodes[a].wire.append(nodes[b])
    nodes[b].wire.append(nodes[a])

for n in nodes[1:] :
    n.sort()
dfs = [nodes[start]]
while dfs :
    node= dfs.pop(0)
    if not node.detected :
        print(node, end=" ")
        dfs= node.wire + dfs
        node.detected= True
print("\n", end="")
# 노드 초기화
for n in nodes[1:] :
    n.reset()
    
bfs= [nodes[start]]
while bfs :
    node= bfs.pop(0)
    if not node.detected :
        print(node, end=" ")
        bfs= bfs + node.wire
        node.detected= True