class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.is_word = True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # 1. Trie me saare words insert karein
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        memo = {}

        # 2. Recursive DFS function
        def dfs(i):
            if i == len(s):
                return 0  # Base case: String khatam, 0 extra chars
            
            if i in memo:
                return memo[i]

            # Option A: Current character ko extra maan kar skip kar do
            res = 1 + dfs(i + 1)

            # Option B: Trie me search karke valid words dhoondo
            curr = trie.root
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    break  # Prefix aage nahi mil sakta, loop stop karo
                
                curr = curr.children[s[j]]
                if curr.is_word:
                    # Valid word mil gaya, best minimum result update karo
                    res = min(res, dfs(j + 1))

            memo[i] = res
            return res

        return dfs(0)