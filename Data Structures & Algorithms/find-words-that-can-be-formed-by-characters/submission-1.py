from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        hm = Counter(chars)
        for w in words:
            w_char_freq = Counter(w)
            if all(hm.get(key,0) >= val for key , val in w_char_freq.items()):
                count += len(w)
        return count

            