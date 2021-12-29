from typing import List
def wordBreak( s: str, wordDict: List[str]) -> bool:

    wordDict.sort( key = lambda i: (len(i)))
    res = s
    for i in range (len(wordDict)):
        ns = len(wordDict[i])            
        for j in range(len(s)):
            k = s[j:j+ns]
            if k == wordDict[i]:
                res= res.replace(k, "")
    if res == "":
        return True
    else:
        return False

print(wordBreak("applepenapple", ["apple", "pen"]))