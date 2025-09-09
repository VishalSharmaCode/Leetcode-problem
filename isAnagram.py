class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def frequencyNumber(items):
            frequency = {}
            for item in items:
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1
            return frequency

# get frequency dictionaries
        k = frequencyNumber(s)
        j = frequencyNumber(t)
        return k==j
        