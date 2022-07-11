class Node:
    def __init__(self, key="", val=""):
        self.key = key
        self.val = val
        self.right = None
        self.left = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head
        self.size = -1
        self.capacity = capacity

    def get(self, key: int) -> int:
        node = self.cache.get(key, -1)
        
        if node == -1: return -1
        
        self.remove_node(node)
        self.add_to_front(node)
        return node.val
            
        
    def put(self, key: int, value: int) -> None:
        self.size += 1
        if self.size < self.capacity:
            node = Node(key, value)
            self.add_to_front(node)
            self.cache[key] = node
        else:
            node = self.cache.get(key, None)
            
            if node:
                node.val = value
                if node.key in self.cache:
                    self.cache.pop(node.key)
                self.remove_node(node)
                self.add_to_front(node)
                self.cache[key] = node
            else:
                node = self.tail.left
                if node.key in self.cache:
                    self.cache.pop(node.key)
                node.val = value
                node.key = key
                self.remove_node(node)
                self.add_to_front(node)
                self.cache[key] = node
                    
        temp = self.head
    
    def add_to_front(self, node):
        node.left = self.head
        node.right = self.head.right
        
        self.head.right.left = node
        self.head.right = node
        
    def remove_node(self, node):
        node.left.right = node.right
        node.right.left = node.left

'''
Time complexity : O(1) both for put and get.

Space complexity : O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.
'''