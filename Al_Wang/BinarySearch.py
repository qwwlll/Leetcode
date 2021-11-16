from typing import List
#### BinarySearch 
#### Time Complexity: O(logn)
#### Space Complexity: O(1) 在原数组上改动
#### ————————————————————————————————————————————————————————数组中第一个等于给定值的元素
### o(n) since we loop through the whole list
def firstEle (nums: List[int], target : int) -> int: 
    for i in range(len(nums)):
        if target == nums[i]:
            return i
    else:
        return -1
nums = [1,3,4,5,6,8,8,8,11,13]
print(firstEle(nums,8))
### other way, by using the binary search
### O(logn):
### leetcode 704 二分查找n
def firstEleBS (nums: List[int], target : int) -> int: 
    low = 0
    high = len(nums) - 1
    while(low <= high):
        mid = low + ((high - low) >> 1)
        if (nums[mid] >= target):
            high = mid - 1
        else:
            low = mid + 1
    
    if (low < len(nums) and nums[low] == target): return low
    else: return -1
print(firstEleBS(nums,8))
### otehr way of B
def firstEleBS1 (nums: List[int], target : int) -> int: 
    low = 0
    high = len(nums)-1
    while(low <= high):
        mid = low + ((high - low) >> 1)
        if (target < nums[mid]):
            high = mid - 1
        elif(target > nums[mid]):
            low = mid + 1
        else:
            if mid == 0 or nums[mid - 1] != target:
                return mid
            else:
                high = mid - 1
    return -1
print(firstEleBS1(nums,8))

#### ————————————————————————————————————————————————————————数组中最后一个等于给定值的元素 
def lastEleBS (nums: List[int], target : int) -> int: 
    low = 0
    high = len(nums)-1
    while(low <= high):
        mid = low + ((high - low) >> 1)
        if (target < nums[mid]):
            high = mid - 1
        elif(target > nums[mid]):
            low = mid + 1
        else:
            if mid == 0 or nums[mid + 1] != target:
                return mid
            else:
                high  = mid + 1
    return -1
print(lastEleBS(nums,8))

#### ————————————————————————————————————————————————————————数组中第一个大于给定值的元素 
def bigEleBS (nums: List[int], target : int) -> int: 
    low = 0
    high = len(nums)
    while low <= high:
        mid = low + ((high - low ) >> 1)
        if (target <= nums[mid]):
            if mid == 0 or nums[mid -1 ] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1
nums1 = [3, 4, 6, 7, 10]
print(bigEleBS(nums1, 5))
      


#### ————————————————————————————————————————————————————————数组中最后一个小于给定值的元素 
def smallEleBS (nums: List[int], target : int) -> int: 
    low = 0 
    high = len(nums)
    while low <= high:
        mid = low + ((high - low) >> 1)
        if (nums[mid] < target):
            if mid == len(nums) -1  or nums[mid + 1 ] > target:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1
    return -1 

nums1 = [3, 4, 6, 7, 10]
print(smallEleBS(nums1, 5))



#### leetcode 33 
#### 搜索旋转排序数组
#### 和第一位比较大小选择进入前半段或后
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(nums: List[int], target: int) -> int:
            low = 0
            hi = len(nums)-1
            while (low <= hi):
                mid = low + ((hi - low) >> 1)
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                    else:
                        hi = mid - 1
            return -1

        if len(nums) <= 5:
            for i in range (len(nums)):
                if nums[i] == target:
                    return i 
            else: return -1
        a = nums.index(max(nums))
        if target >= nums[0]:
            n = BS(nums[0:a+1],target)
            if n != -1 :
                return n
            else: 
                return -1
        else:
            n = BS(nums[a+1:],target)
            if n != -1 :
                return n + len(nums[0:a+1])
            else: 
                return -1




#### NC 74， 数字在升序数组中出现的次数
#### 计算target 前后的index 相减 再-1 既得 target 数量
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        n = len(data)
        low, high  = 0, n-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                high = mid - 1
        sma = high
        low, high  = 0, n-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                low = mid  + 1
        big = low
        res =  big - sma - 1
        if res > 0:
            return res
        else: return 0

###leetcode 34 在排序数组中查找元素的第一个和最后一个位置
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        res = []
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                low = mid + 1 #### 找到上边界 -1 得排列最高的target index
        big = low - 1
        low, high = 0, len(nums)-1
        while low <= high:
            mid = low + ((high - low) >> 1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1 #### 找到下边界 +1 得排列最底的target index
        sam = high + 1
        return [sam, big]
        
#### leetcode 35 搜索插入位置
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target > nums[n-1]:
            return n
        low, high = 0, n-1
        while low <= high:
            mid = low + ((high- low )>>1)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        return low

### leetcode 852 寻找峰顶
### 二分查找
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 3:
            return 1        
        low, high = 0, len(arr)-1
        while low <= high:
            mid = low + ((high - low ) >>1 )
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            elif arr[mid]> arr[mid+1] and arr[mid] < arr[mid-1]:
                high = mid - 1
            elif arr[mid]< arr[mid+1] and arr[mid] > arr[mid-1]:
                low = mid + 1
        return low

### leetcode 658 找k个最接近的数
### 闭区间二分
class Solution(object):
    def findClosestElements(self, arr, k, x):
        left = 0
        right = len(arr) - k - 1
        while (left <= right) :
            mid = left + (right - left) // 2
            if (x - arr[mid] > arr[mid + k] - x) :
                left = mid + 1
            else :
                right = mid - 1
        return arr[left : left + k]

### leetcode 69 squt
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        mi, mx, res = 0, x, 0
        while mi <= mx:
            mid = (mi + mx) //2
            if mid * mid <= x:
                res = mid
                mi = mid + 1
            else:
                mx = mid - 1
        return res
    
### leetcode 287寻找重复的数
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left = 1
        right = len(nums)
        while left < right:
            mid = left + ((right - left)>>1)
            cnt = 0
            for num in nums:
                if num <= mid:
                   cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right