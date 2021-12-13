from typing import List
def calNum(a: int, lt: List[int]):
    if a <= 0:
        return 0
    res = []
    index = 0
    while index < a:
        num = 0
        nums = lt.copy()
        nums[index] = 0
        for i in range(a):
            if (a - abs(i-index)) <= nums[i]:
                num += nums[i] - (a - abs(i-index))
        res.append(num)
        index += 1
    return res

# while 1:
#     try:
#         a = int(input())
#         lt = list(map(int,input().split()))
#         print(calNum(a, lt))
#     except:
#         break 


a = 5
lt = [10 ,1 ,10 ,10 ,10]
print(calNum(a, lt))