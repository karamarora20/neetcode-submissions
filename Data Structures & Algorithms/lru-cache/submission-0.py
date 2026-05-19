class Node:
    def __init__(self,val=0):
        self.val=val
        self.nxt=None
        self.prev=None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.prev = self.head
        self.n=0
        self.cap=capacity
        self.items={}

    def remove(self, node):
        prev = node.prev
        nxt = node.nxt
        prev.nxt = nxt
        nxt.prev = prev

    def insert(self,node):
        node.nxt = self.head.nxt
        node.prev = self.head
        self.head.nxt.prev = node
        self.head.nxt = node
        
    def get(self, key: int) -> int:
        if key not in self.items:
            return -1
        
        val,node=self.items[key]
        self.remove(node)
        self.insert(node)
        return val


    def put(self, key: int, value: int) -> None:
        new_n=Node(key)
        if key in self.items:
            self.remove(self.items[key][1])
        node=Node(key)
        self.insert(node)
        self.items[key]=(value,node)
        if len(self.items) > self.cap:
        # remove LRU (node before tail)
            lru = self.tail.prev
            self.remove(lru)
            del self.items[lru.val]



        
