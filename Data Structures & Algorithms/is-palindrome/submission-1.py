class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()
        return cleaned_text == cleaned_text[::-1]