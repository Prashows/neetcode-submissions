class Node:

    def __init__(self,key :int ,val :int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        
        self.cap = capacity
        self.lru_cache = {}
        self.left = Node(0,0)
        self.right = Node(0,0)

        self.left.next = self.right
        self.right.prev = self.left
    


    def remove(self , node : Node):

        prevd = node.prev
        nextt= node.next
        prevd.next = nextt
        nextt.prev = prevd
    
    def insert(self , node:Node):

        prev = self.right.prev
        nextt = self.right

        prev.next = nextt.prev = node
        node.prev = prev
        node.next = nextt
        



    def get(self, key: int) -> int:
        if key in self.lru_cache:
            
            self.remove(self.lru_cache[key])
            self.insert(self.lru_cache[key])

            return self.lru_cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.lru_cache:
            self.remove(self.lru_cache[key])
            
        self.lru_cache[key]=Node(key,value)
        self.insert(self.lru_cache[key])
        if len(self.lru_cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.lru_cache[lru.key]

        
