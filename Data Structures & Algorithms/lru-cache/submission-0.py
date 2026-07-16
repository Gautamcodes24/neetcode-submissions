class Node:
    def __init__(self , key , val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right = Node(0,0)
        self.left = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
        
    def _remove(self , node):
        pre = node.prev
        nxt = node.next
        nxt.prev = pre
        pre.next = nxt
    def _insert(self , node):
        nxt , pre = self.right , self.right.prev
        nxt.prev = node
        node.prev = pre
        node.next = nxt
        pre.next = node
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key , value)
        self._insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self._remove(lru)
            del self.cache[lru.key]

        
