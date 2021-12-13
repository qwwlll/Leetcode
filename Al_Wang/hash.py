### hash 一致性哈希算法：
### https://www.zsythink.net/archives/1182
def AllRange(listx, start, end):
    if start == end:
        for i in listx:
            print(i,end = '')
        print()
    for m in range(start,end+1):
        listx[m],listx[start] = listx[start],listx[m]
        AllRange(listx, start+1, end)
        listx[m],listx[start] = listx[start],listx[m]
list1 = [1,2,3,4]
AllRange(list1,0, 3)
# def check(n: int, m:int) -> int:
#     if n == 0:
#         return 0
#     if m == 0:
#         return 0
#     nums = str(n)
#     def strAll(s: str):
#         res = []
#         if len(s) <= 1:
#             return [s]
#         res = []
#         for i in range(len(s)):
#             for j in strAll(s[0:i] + s[i+1:]):
#                 res.append(s[i] + j)
#         return res
#     res = set(strAll(nums))
#     count = 0
#     for i in res:
#         if int(i) %m == 0:
#             count += 1
#     return count
# print(check(112,4))