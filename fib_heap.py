import math
import numpy as np


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.parent = None
        self.child = None
        self.left = None
        self.right = None
        self.degree = 0


class FibHeap:
    def __init__(self):
        self.size = 0
        self.min = None
        self.root = None
        
    
    def insert(self, key, value):
        new_node = Node(key, value)
        
        if self.size == 0:
            new_node.left = new_node
            new_node.right = new_node
            self.root = new_node
        else:
            new_node.right = self.root.right
            new_node.left = self.root
            self.root.right.left = new_node
            self.root.right = new_node
            
        self.size += 1
            
        if self.min is None or self.min.key > new_node.key:
            self.min = new_node
            
            
    def node_to_root_list(self, node):
        if self.root is None:
            self.root = node
        else:
            node.right = self.root.right
            node.left = self.root
            self.root.right.left = node
            self.root.right = node
            
    
    def get_min(self):
        return self.min
    
    
    def remove_node(self, node):
        if self.root == node:
            self.root = node.right
            
        node.left.right = node.right
        node.right.left = node.left
        
        
    def childs_to_root_list(self, parent):
        child = parent.child
        childrens = self.get_nodes_list(child)
        for c in childrens:
            self.node_to_root_list(c)
            c.parent = None
        
        
    def consolidate(self):
        degrees = [None] * int(math.log(self.size) * 2)
        nodes = self.get_nodes_list(self.root)
        for i in range(0, len(nodes)):
            curr_node = nodes[i]
            d = curr_node.degree
            while degrees[d] != None:
                collision_node = degrees[d]
                
                if curr_node.key > collision_node.key:
                    tmp = curr_node
                    curr_node, collision_node = collision_node, tmp
                
                self.remove_node(collision_node)
                collision_node.left = collision_node
                collision_node.right = collision_node
        
                self.merge_with_child_list(curr_node, collision_node)
                curr_node.degree += 1
                collision_node.parent = curr_node
                
                degrees[d] = None
                d += 1
                
            degrees[d] = curr_node
            
        nodes = self.get_nodes_list(self.root)
        for n in nodes:
            if n.key < self.min.key:
                self.min = n
        
        
    def merge_with_child_list(self, parent, node):
        if parent.child is None:
            parent.child = node
        else:
            node.right = parent.child.right
            node.left = parent.child
            parent.child.right.left = node
            parent.child.right = node
    
    
    def extract_min(self):
        minimum_node = self.min
        
        if minimum_node is not None:
            if minimum_node.child is not None:
                self.childs_to_root_list(minimum_node)
            
            self.remove_node(minimum_node)
            
            if self.size == 1:
                self.min = None
                self.root = None
            else:
                self.min = minimum_node.right
                self.consolidate()
                
            self.size -= 1
            
        return minimum_node
            
    
    def get_nodes_list(self, head):
        res = [head]
        current = head.right
        while current != head:
            res.append(current)
            current = current.right
        return res           
        

if __name__ == '__main__':
    fh = FibHeap()
    true_list = []
    for i in range(1000):
        x = np.random.randint(1, 10000)
        fh.insert(x, 1)
        true_list.append(x)
        
    true_list.sort()
    
    my_list = []
    while fh.size != 0:
        my_list.append(fh.extract_min().key)
        
    print(my_list == true_list)
    