from typing import Counter, List
### 给string 进行不同需求的排序
def sortingStr(n: List[str]) -> List[str]:
### 将list n 先以长度后以字符序排序

#    n.sort(key= lambda i :(len(i), i))

### 将list n 先以字符序排序后以长度
#    n.sort(key = lambda i:(i, len(i))) ### 先后顺序matters！

### 先将list n 以 a 的重复次数排序 后以长度后以字符序排序
    dic = {}
    def counting(x):
        return x.count('a')

###    result = sorted(dic.items(), key= lambda x: x[1],reverse= True)
### 多条件sort
    res = sorted(n, key = lambda i: (counting(i),len(i),i),reverse= True)
    return res
    



n = ['asdas', 'asfw', 'efa', 'hfeafa', 'ddefaf','abc','ac','aacs','abbcs']
print(sortingStr(n))
### leetcode 4 + 451