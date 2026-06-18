from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        hm = Counter(chars)
        print('Hm',hm)
        count = 0
        for w in words:
            w_count = Counter(w)
            print(w_count)
            cnt = 0
            for key , val in w_count.items():
                print('finding key',key)
                if hm.get(key,0) >= val:
                    cnt += val
                    print('Char found in hm',key)
                else:
                    break
            count += cnt if len(w) == cnt else 0
        return count
            