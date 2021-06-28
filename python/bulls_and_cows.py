class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_hash = {str(i): 0 for i in range(10)}
        guess_hash = {str(i): 0 for i in range(10)}

        bulls, cows = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_hash[s] += 1
                guess_hash[g] += 1

        for sh, gh in zip(secret_hash.values(), guess_hash.values()):
            if sh != 0 and gh != 0:
                cows += min(sh, gh)

        return f"{bulls}A{cows}B"


s = Solution()
print(s.getHint("1807", "7810"))
print(s.getHint("1123", "0111"))
print(s.getHint("1", "0"))
print(s.getHint("1", "1"))
print(s.getHint("0", "1"))
print(s.getHint("0", "1"))