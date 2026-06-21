class MyHashMap:

    def __init__(self):
        self.kachra_seth = dict()        

    def put(self, key: int, value: int) -> None:
        self.kachra_seth[key] = value
        

    def get(self, key: int) -> int:
        return self.kachra_seth.get(key,-1)
        

    def remove(self, key: int) -> None:
        if key in self.kachra_seth:
            del self.kachra_seth[key]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)