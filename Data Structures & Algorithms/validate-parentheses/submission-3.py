class Solution:
    def isValid(self, s: str) -> bool:
        bracket_stack = []

        if len(s) < 2:
            return False

        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in ('(', '{', '['):
                bracket_stack.append(c)
            elif c in (')', '}', ']'):
                if len(bracket_stack) == 0:
                    return False
                last_bracket = bracket_stack.pop()
                if last_bracket != bracket_map.get(c):
                    return False
            else:
                return False

        return len(bracket_stack) == 0