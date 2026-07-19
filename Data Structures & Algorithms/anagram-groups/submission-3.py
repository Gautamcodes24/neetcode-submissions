from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for w in strs:
            sorted_w = "".join(sorted(w))
            print(sorted_w)
            if sorted_w in hm:
                # 1. Get the existing list, or default to an empty list if it doesn't exist yet
                current_list = hm.get(sorted_w, [])

                # 2. Append the new item
                current_list.append(w)

                # 3. Put the updated list back into the dictionary
                hm[sorted_w] = current_list

            else:
                hm[sorted_w] = [w]
        return [val for _ , val in hm.items()]

        
        
