from typing import List
def rotate( nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        new_nums =[]

        for i in range(n-k, n):
            new_nums.append(nums[i])
        for i in range(n-k):
            new_nums.append(nums[i])
        nums = new_nums
        return nums

lt =[1,2,3,4,5,6,7]
k = 3
print(rotate(lt, k))