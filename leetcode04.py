class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1 + nums2)     ##将两个有序数组相合并 然后 排序
        x = len(nums) %2       ## 检查总数奇偶
        res = 0
        if x == 0:
            res = (nums[int(len(nums)/2)]+nums[(int(len(nums)/2))-1])/2
        else:
            
            res =  nums[int(len(nums)/2)]
        return res