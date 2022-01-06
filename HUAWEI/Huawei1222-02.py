from typing import List
#### 列车订票系统
# while 1:
#     try:
#         a, b, lt = int(input()), int(input()), input()

#     except:
#         break

# a, b, stops = int(input()), int(input()), input()

def oreder(a: int, b: int, stops: List[List[int]]):
    res = []
    #a = stop_num
    #b = seat_num
    stops1 = stops.sort(key = lambda i : int(stops[i][1]))
    return print(stops1)



a = 10
b = 100
stops = [[0,5],[0,9],[6,10]]
oreder(a, b, stops)