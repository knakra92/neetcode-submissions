class Solution:

    def calculate_char_freq_in_word(self, word: str):
        char_freq: dict[str, int] = {}
        
        for c in word:
            if c in char_freq:
                char_freq[c] += 1
            else:
                char_freq[c] = 1

        return char_freq

    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        char_freq_one: dict[str, int] = self.calculate_char_freq_in_word(s)
        char_freq_two: dict[str, int] = self.calculate_char_freq_in_word(t)

        if len(char_freq_one) != len(char_freq_two):
            return False

        for k, v in char_freq_one.items():
            if k not in char_freq_two:
                return False
            elif char_freq_one[k] != char_freq_two[k]:
                return False

        return True
