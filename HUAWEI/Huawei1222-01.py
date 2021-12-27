from typing import List
#### 房间抽奖
#### question 1
#### inputs:
#### 4,21
#### 2,1,4,3
#### outputs:
#### 9
def bonus(a: List[int], b: List[int]):
    room_num = a[0]
    coin_num = a[1]
    count = 0
    round = sum(b)
    if coin_num < min(b):
        count = 0
    if coin_num > round:
        more = coin_num % round
        rds = coin_num // round
        for i in range(room_num):
            if b[i] <= more:
                count += 1
                more -= b[i]
        count = count + rds * room_num

    elif coin_num == round:
        count = room_num
    else:
        for i in range(room_num):
            if b[i] <= coin_num:
                count += 1
                coin_num -= b[i]
    return count


a = [4,10]
b = [2,91,4,3]
print(bonus(a, b))


# while 1:
#     try:
#         # a  = list(map(int, input().split(",")))
#         # b  = list(map(int, input().split(",")))
#         a = [4,21]
#         b = [2,1,4,3]
#         print(bonus(a, b))
       
#     except:
#         break