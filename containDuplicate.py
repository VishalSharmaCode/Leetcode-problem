class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        def frequencyNumber(items):
            frequency = {}
            for item in items:
                if item in frequency:
                    frequency[item]+=1
                else:
                    frequency[item] =1
            return frequency 
        x = frequencyNumber(nums)
        y = list(x.values())
        for i in y:
            if i > 1:
                return True
        return False