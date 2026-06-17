class Solution:
    def largestGoodInteger(self, num: str) -> str:
        best_digit = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                best_digit = max(num[i], best_digit)
        return best_digit * 3 if best_digit else ""