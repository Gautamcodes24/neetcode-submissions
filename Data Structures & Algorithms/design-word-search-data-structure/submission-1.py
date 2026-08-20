class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.is_end = True
    def search(self, word: str) -> bool:
        def dfs(indx , root):
            curr = root
            for i in range(indx , len(word)):
                w = word[i]
                if w == ".":
                    for node in curr.children.values():
                        if dfs(i+1 , node):
                            return True
                    return False
                else:
                    if w not in curr.children:
                        return False
                    curr = curr.children[w]
            return curr.is_end
        return dfs(0,self.root)

            
        
