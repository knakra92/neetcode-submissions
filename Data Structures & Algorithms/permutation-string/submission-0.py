class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_char_freq = {}
        current_window_char_freq = {}

        if len(s1) > len(s2):
            return False

        for s in s1:
            s1_char_freq[s] = s1_char_freq.get(s, 0) + 1

        for i in range(len(s1)):
            current_window_char_freq[s2[i]] = current_window_char_freq.get(s2[i], 0) + 1

        if current_window_char_freq == s1_char_freq:
            return True

        left = 0
        right = len(s1)

        for right in range(len(s1), len(s2)):
            current_window_char_freq[s2[right]] = current_window_char_freq.get(s2[right], 0) + 1
            current_window_char_freq[s2[left]] = current_window_char_freq.get(s2[left], 0) - 1
            if current_window_char_freq[s2[left]] == 0:
                current_window_char_freq.pop(s2[left])
            left += 1

            if s1_char_freq == current_window_char_freq:
                return True

        return False
        