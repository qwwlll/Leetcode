#### matching the strings
#### bf and rk
#### bf
from time import time
def Bruteforce(A: str, B: str) -> bool:
    n = len(A)
    m = len(B)
    if n <= m:
        if n == m :
            return True
        else:
            return False
    for i in range(n - m + 1):
        for j in range(m):
            if A[i+j] == B[j]:
                if j == m - 1:
                    
                    return True
                else:
                    continue
            else:
                break
    return False
def getHash(s, start, end):
    while start <= end:
        ret = 0
        for i in s[start:end+1]:
            ret = ret + ord(i)
        return ret  

def RabinKarp(A,B):
    n = len(A)
    m = len(B)   
    if n <= m:
        if n == m :
            return True
        else:
            return False 
    ## turning hash for the B:
    xm = getHash(B, 0, m-1)
    hashBig = [None] * (n-m+1)
    hashBig[0] = getHash(A, 0, m-1)
    for i in range(1, n-m+1):
        hashBig[i] = hashBig[i-1]- getHash(A, i-1, i-1) + getHash(A, i+m-1, i+m-1)
    for i, x in enumerate(hashBig):
        if x == xm:
            if B == A[i:i+m]:
                return True
            else:
                continue
    return False
m_str = 'thequickbrownfoxjumpsoverthelazydog'
p_str = 'jump'
print(Bruteforce(m_str,p_str))
print(RabinKarp(m_str,p_str))




##### 时间比较

x_str = 'a'*10000
y_str = 'a'*200+'b'
t = time()
print('[bf] result:', Bruteforce(x_str, y_str))
print('[bf] time cost: {0:.5}s'.format(time()-t))

t = time()
print('[rk] result:', RabinKarp(m_str, p_str))
print('[rk] time cost: {0:.5}s'.format(time()-t))