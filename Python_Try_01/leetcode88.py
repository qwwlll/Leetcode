class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:]= nums2
        nums1.sort()



#除掉nums1 m位后面
#插入nums2 
#sort