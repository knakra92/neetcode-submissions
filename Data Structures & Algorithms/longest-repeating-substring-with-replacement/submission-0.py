class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        max_length = min(len(s), k + 1)
        max_freq = 1
        char_freq: dict[str, int] = {}

        while right < len(s):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1

            max_freq = max(char_freq[s[right]], max_freq)

            curr_window_length = right - left + 1

            if curr_window_length - max_freq <= k:
                max_length = max(max_length, curr_window_length)
                right += 1
            else:
                char_freq[s[left]] = char_freq[s[left]] - 1
                left += 1
                right += 1


        return max_length