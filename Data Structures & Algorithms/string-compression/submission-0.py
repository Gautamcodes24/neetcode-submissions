class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        write = 0
        char_len = len(chars)
        while i < char_len:
            c = chars[i]
            length = 0
            while i < char_len and c == chars[i]:
                length += 1
                i += 1
            chars[write] = c
            write += 1
            if length > 1:
                for d in str(length):
                    chars[write] = d
                    write += 1
        return write