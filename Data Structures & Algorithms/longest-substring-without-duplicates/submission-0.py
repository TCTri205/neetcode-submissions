class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        res = 0
        i = 0

        for j in range(len(s)):
            if s[j] not in se:
                se.add(s[j])
                res = max(res, j-i+1)
            else:
                while s[j] in se:
                    se.remove(s[i])
                    i += 1
                se.add(s[j])
        return res