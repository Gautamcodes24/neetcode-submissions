class MyHashSet:

    def __init__(self):
        self.kachra_seth = set()
        

    def add(self, key: int) -> None:
        self.kachra_seth.add(key)
        

    def remove(self, key: int) -> None:
        self.kachra_seth.discard(key)

    def contains(self, key: int) -> bool:
        return key in self.kachra_seth
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)