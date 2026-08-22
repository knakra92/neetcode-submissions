class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for i in temperatures]

        for idx, temp in enumerate(temperatures):
            if len(stack) == 0:
                stack.append(temp)
            else:
                if temp > stack[-1]:
                    counter = 1
                    while len(stack) > 0 and temp > stack[-1]:
                        if result[idx-counter] == 0:
                            result[idx-counter] = counter
                            stack.pop()
                        counter += 1

                stack.append(temp)

        return result
