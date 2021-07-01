class Up:
    def go(self, x, y):
        return x, y + 1

    def left(self, solution):
        solution.state = Left()

    def right(self, solution):
        solution.state = Right()


class Left:
    def go(self, x, y):
        return x - 1, y

    def left(self, solution):
        solution.state = Down()

    def right(self, solution):
        solution.state = Up()


class Right:
    def go(self, x, y):
        return x + 1, y

    def left(self, solution):
        solution.state = Up()

    def right(self, solution):
        solution.state = Down()


class Down:
    def go(self, x, y):
        return x, y - 1

    def left(self, solution):
        solution.state = Right()

    def right(self, solution):
        solution.state = Left()


class Solution:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.state = Up()

    def isRobotBounded(self, instructions: str) -> bool:
        for step in range(4):
            print(self.x, self.y)
            for instruction in instructions:
                if instruction == "G":
                    self.x, self.y = self.state.go(self.x, self.y)
                if instruction == "L":
                    self.state.left(self)
                if instruction == "R":
                    self.state.right(self)

            if self.x == 0 and self.y == 0:
                return True

        return False


s = Solution()
print(s.isRobotBounded("GGLLGG"))
s = Solution()
print(s.isRobotBounded("GG"))
s = Solution()
print(s.isRobotBounded("GL"))