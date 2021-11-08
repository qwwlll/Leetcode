class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        repeatDict = {}    ##用一个字典来放置
        for num in nums:
            if num not in repeatDict:
                repeatDict[num] = 1
            else:
                return num