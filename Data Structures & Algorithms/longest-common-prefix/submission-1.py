class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        shortest = len(min(strs, key=len))
        diff = False
        while i < shortest:
            char = strs[0][i]
            for j in range(len(strs)):
                if char != strs[j][i]:
                    diff = True
                    break
            if not diff:
                i += 1
            else:
                break
        return strs[0][:i]