from typing import DefaultDict, List
def kill_jc(pid: List[int], ppid: List[int],kill: int):
    n = len(ppid)
    dic = DefaultDict(list)
    for i in range(n):
        dic[ppid[i]].append(pid[i])
    
    stack = []
    end = []
    stack.append(kill)
    while stack:
        kb = stack[-1]
        end.append(kb)
        stack.pop()
        if dic[kb]:
            stack = stack + dic[kb]
            dic[kb] = []
    return end




pid = [1,3,10,5] 
ppid = [3,0,5,3]
kill = 5
print(kill_jc( pid,ppid, kill))