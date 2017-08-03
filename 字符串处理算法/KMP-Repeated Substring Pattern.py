class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        next, j = [0], 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                next.append(j + 1)
                j += 1
            else:
                next.append(0)
        print(next)
        return next[-1] > 0 and next[-1] % (len(s) - next[-1]) == 0
Solution().repeatedSubstringPattern("abababaabababaabababa")