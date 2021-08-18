from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if not stack:
                stack.append(asteroid)
            else:
                if asteroid > 0:
                    stack.append(asteroid)
                if asteroid < 0:
                    if stack[-1] > 0:
                        while stack and 0 < stack[-1] < abs(asteroid):
                            stack.pop()
                        if stack and stack[-1] == abs(asteroid):
                            stack.pop()
                        elif (stack and stack[-1] < 0) or not stack:
                            stack.append(asteroid)
                    else:
                        stack.append(asteroid)

        return stack


s = Solution()

print(s.asteroidCollision([5, 10, -5]))
print(s.asteroidCollision([8, -8]))
print(s.asteroidCollision([8, -7]))
print(s.asteroidCollision([8, -9]))
print(s.asteroidCollision([-1, -8]))
print(s.asteroidCollision([10, 2, -5]))
print(s.asteroidCollision([-2, -1, 1, 2]))
print(s.asteroidCollision([-2, -1, 1, 2, -1]))
print(s.asteroidCollision([-2, -1, 1, 2, -3, 3]))