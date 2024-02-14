import sys
sys.setrecursionlimit(10**6)

#N = int(input())
#n_arr = list(map(int, input().split(' ')))
#M = int(input())
#m_arr = list(map(int, input().split(' ')))
import random
n_arr = [random.randint(-2**30, (2**30) -1) for i in range(100000)]
m_arr = [random.randint(-2**30, (2**30) -1) for i in range(100000)]

class Binary_tree :
    def __init__(self, arr) :
        self.arr = arr
        self.head = None
        self.cur = None
        self.make_nodes()
    
    def make_nodes(self) :
        for value in self.arr :
            self.append(value)
            
    def append(self, value) :
        if self.head == None :
            self.head = Node(value)
            self.cur = self.head
        else :
            # 값이 현재 노드보다 큰 경우
            if self.cur.value < value :
                if self.cur.right == None :
                    self.cur.right = Node(value)
                    self.cur = self.head
                else :
                    self.cur = self.cur.right
                    self.append(value)
            # 값이 현재 노드보다 작은 경우
            else :
                if self.cur.left == None :
                    self.cur.left = Node(value)
                    self.cur = self.head
                else :
                    self.cur = self.cur.left
                    self.append(value)
    
    def find(self, value) :
        # 값을 찾은 경우
        if self.cur.value == value :
            print('1')
            self.cur = self.head
        
        # 값을 찾아야 하는 경우
        else :
            # 현재 노드보다 값이 큰 경우
            if self.cur.value < value :
                if self.cur.right == None :
                    print('0')
                    self.cur = self.head
                else :
                    self.cur = self.cur.right
                    self.find(value)
            
            # 현재 노드보다 값이 작은 경우
            else :
                if self.cur.left == None :
                    print('0')
                    self.cur = self.head
                else :
                    self.cur = self.cur.left
                    self.find(value)
                
class Node :
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None
def node_to_list(node) :
    left, right = [], []
    if node.left != None :
        left = node_to_list(node.left)
    value = node.value
    if node.right != None :
        right = node_to_list(node.right)
    return [*left, value, *right]

new_arr = []
def re_array(array) :
    length = len(array)
    if length == 0 :
        return 
    else :
        index = length // 2
        new_arr.append(array[index])
        re_array([*array[:index]])
        re_array([*array[index+1:]])

import time
start = time.time()
b = Binary_tree(n_arr)
for num in m_arr :
    b.find(num)
end =time.time()
before = end - start

start = time.time()
b = Binary_tree(n_arr)
sorted_arr = node_to_list(b.head)
re_array(sorted_arr)
b = Binary_tree(new_arr)
for num in m_arr :
    b.find(num)
end = time.time()
new = end - start
print(f'기존 방법 : {round(before, 2)}')
print(f'새 방법 : {round(new, 2)}')
