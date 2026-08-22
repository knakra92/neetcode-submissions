class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in ('+', '-', '*', '/'):
                second_num = stack.pop()
                first_num = stack.pop()
                expression_result = None
                if token == '+':
                    expression_result = int(second_num) + int(first_num)
                elif token == '-':
                    expression_result = int(first_num) - int(second_num)
                elif token == '*':
                    expression_result = int(second_num) * int(first_num)
                elif token == '/':
                    expression_result = int(first_num) / int(second_num)

                stack.append(expression_result)
            else:
                stack.append(token)

        return int(stack[0])