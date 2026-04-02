class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in s:
            if i in freq:
                freq[i]+=1
            else:
                freq[i] =1
        uniq = []
        for i in freq:
            if freq[i] == 1:
                uniq.append(i)
        if not uniq:
            return -1
        for i in range(len(s)):
            if s[i] == uniq[0]:
                return i