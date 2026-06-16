from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for indx,w in enumerate(strs):
            srt_w = "".join(sorted(w))
            if srt_w not in hm:
                hm[srt_w] = []
            hm[srt_w].append(strs[indx])
        return [val for val in hm.values()]
