class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        res = ""
        tmp = strs[0]
        min_len = 201

        for s in strs:
            min_len = min(min_len, len(s))

        while i < min_len:
            c = True
            for j in range(1, len(strs)):
                if tmp[i] != strs[j][i]:
                    c = False
                    break
            if c: 
                res += tmp[i]
                i += 1
            else:
                break
        return res