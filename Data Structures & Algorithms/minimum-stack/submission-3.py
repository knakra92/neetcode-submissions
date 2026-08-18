class MinStack:

    def __init__(self):
        self.nums = []
        self.min_nums = []
        
    def push(self, val: int) -> None:
        self.nums.append(val)
        min_val = min(val, self.min_nums[-1] if self.min_nums else val)
        self.min_nums.append(min_val)

    def pop(self) -> None:
        self.nums.pop()
        self.min_nums.pop()

    def top(self) -> int:
        return self.nums[-1]

    def getMin(self) -> int:
        return self.min_nums[-1]
