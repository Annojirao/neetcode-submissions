class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) < 1:
            return prefix
        elif len(strs) ==1:
            return strs[0]
        for i in range(len(strs[0])):
            count = 0
            for s in strs[1:]:
                count = count + 1
                if s and len(s) > i and strs[0][i] == s[i]:
                    continue
                else:
                    return prefix
            if count == len(strs) - 1:
                prefix += strs[0][i]
        return prefix