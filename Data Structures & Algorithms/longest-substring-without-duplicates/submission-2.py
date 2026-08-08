class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left = 0
        right = 1
        current_chars: set = set()
        current_chars.add(s[left])
        max_length = 1

        while right < len(s):
            if s[right] in current_chars:
                while s[right] in current_chars:
                    current_chars.remove(s[left])
                    left += 1
                current_chars.add(s[right])
            else:
                current_chars.add(s[right])

            max_length = max(max_length, len(current_chars))

            right += 1

        return max_length