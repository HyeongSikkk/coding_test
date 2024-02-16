class BinaryTree :
    def __init__(self, targets) :
        self.targets = targets
        self.head = None
        self.cur = None
        for arr in targets :
            self.append(arr)
        
    def append(self, arr) :
        if self.head == None :
            self.head = Node(arr)
            self.cur = self.head
            
        else :
            # 노드의 값보다 더 큰 경우
            if self.cur.value < arr[0] :
                if self.cur.right == None :
                    self.cur.right = Node(arr)
                    self.cur = self.head
                
                else :
                    self.cur = self.cur.right
                    self.append(arr)
            else :
                if self.cur.left == None :
                    self.cur.left = Node(arr)
                    self.cur = self.head
                else :
                    self.cur = self.cur.left
                    self.append(arr)

class Node :
    def __init__(self, arr) :
        self.arr = arr
        self.value = arr[0]
        self.left = None
        self.right = None

def node_to_list(node) :
    left, middle, right = [], [], []
    if node.left != None :
        left = node_to_list(node.left)
    middle.append(node.arr)
    if node.right != None :
        right = node_to_list(node.right)
    return [*left, *middle, *right]