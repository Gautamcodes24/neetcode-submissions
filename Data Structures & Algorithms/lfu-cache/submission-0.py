class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0
    def length(self):
        return self.size
    def pushRight(self, node):
        prev = self.right.prev
        prev.next = node
        node.prev = prev
        node.next = self.right
        self.right.prev = node
        self.size += 1
    def pop(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        node.prev = None
        node.next = None
        self.size -= 1
    def popLeft(self):
        if self.length() == 0:
            return None
        node = self.left.next
        self.pop(node)
        return node
class LFUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.lfuCnt = 0
        self.nodeMap = {} # Map key -> node
        # Map frequency -> linkedlist of nodes
        self.listMap = defaultdict(LinkedList)
    def counter(self, node):
        cnt = node.freq
        self.listMap[cnt].pop(node)
        if cnt == self.lfuCnt and self.listMap[cnt].length() == 0:
            self.lfuCnt += 1
        node.freq += 1
        self.listMap[node.freq].pushRight(node)
    def get(self, key: int) -> int:
        if key not in self.nodeMap:
            return -1
        node = self.nodeMap[key]
        self.counter(node)
        return node.val
    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.val = value
            self.counter(node)
            return
        if len(self.nodeMap) == self.cap:
            node = self.listMap[self.lfuCnt].popLeft()
            self.nodeMap.pop(node.key)
        node = ListNode(key, value)
        self.nodeMap[key] = node
        self.listMap[1].pushRight(node)
        self.lfuCnt = 1