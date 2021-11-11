from typing import List
## bubble sort/ 冒泡排序 // 原地排序 // 稳定
## Time complexity: O(n^2) // B_case: O(n) W_case: O(n^2) Avg: O(n^2)
## Space complexity:O(1) // 原地排序，所以空间复杂度就是1
def bubble(a:List[int]):
    n = len(a)
    if n <= 1:
        return a 
    for i in range(n):
        swapped = False
        for j in range (n - i - 1):
            if a [j] > a [j + 1]:
                a[j], a[j+1] = a[j+1], a[j] ## 前后比较然后交换
                swapped = True
        if not swapped:
            break
    return a
print([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9])
print(bubble([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9]))


## insertion sort/ 插入排序 // 原地排序 // 稳定
## Time complexity: O(n^2) // B_case: O(n) W_case: O(n^2) Avg: O(n^2)
## Space complexity:O(1) // 原地排序，所以空间复杂度就是1
def insertion(a: List[int]):
    n = len(a)
    if n <= 1: return a
    for i in range(1, n):
        val = a[i]
        j = i-1 
        while j >= 0 and a[j] > val:
            a[j + 1] = a[j]
            j = j - 1 
        a[j+1] = val
    return a
print([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9])
print(insertion([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9]))

## selection sort/ 选择排序 // 原地排序 // 不稳定
## Time complexity: O(n^2) // B_case: O(n^2) W_case: O(n^2) Avg: O(n^2)
## Space complexity:O(1) // 原地排序，所以空间复杂度就是1
def selection(a : List[int]):
    n = len(a)
    if n <= 1: return a
    for i in range (n):
        min_index = i
        min_val = a[i]
        for j in range(i,n):
            if a[j] < min_val:
                min_index = j
                min_val = a[j]
        a[i], a[min_index] = a[min_index], a[i]
    return a
            



print([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9])
print(selection([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9]))


##merge sort/ 归并排序 // 非原地排序 // 稳定
## Time complexity: O(nlogn) // B_case: O(nlogn) W_case: O(nlogn) Avg: O(nlogn)
## Space complexity:O(n) // 非原地排序
def mergeSort(a: List[int]):
    n = len(a)
    mergeb(a, 0, n-1)
    return a 
def mergeb(a:List[int],low:int, high: int):
    if low < high:
        mid = low + (high-low)//2 
        mergeb(a, low , mid)
        mergeb(a, mid+1, high)
        merge(a, low, mid, high)
def merge(a: List[int], low: int, mid: int, high: int):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end + 1])
    a[low:high + 1] = tmp


print([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9])
print(mergeSort([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9]))


import random
##quick sort/ 快速排序 // 原地排序 // 不稳定
## Time complexity: O(nlogn) // B_case: O(nlogn) W_case: O(n^2) Avg: O(nlogn)
## Space complexity:O(1) // 原地排序，所以空间复杂度就是1
def quicksort(a: List[int]):
    n = len(a)
    quicksortb(a, 0, n-1)
def quicksortb(a: List[int], low: int, high: int):
    if low < high:
        k = random.randint(low, high)
        a[low], a[k] = a[k], a[low]
        m = parti(a,low, high)
        quicksortb(a, low, m-1)
        quicksortb(a, m+1, high)
def parti(a: List[int], low: int, high: int):
    pivot , j = a[low], low
    for i in range(low +1, high+ 1):
        if a[i]<= pivot:
            j = j + 1
            a[i], a[j] = a[j], a[i]
    a[low], a[j] = a[j], a[low]
    return j
print([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9])
print(mergeSort([2,3,4,31,3,1,4,2,5,6,721,3,4,2,7,9]))