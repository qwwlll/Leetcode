from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#### leetcode 94 105 106 450 889
### 二叉树先序<->树的先根<->森林的先序
### 二叉树中序<->树的后根<->森林的中序



### leetcode 94 中序遍历 Binary Tree
class Solution:
    def inorderTraversal(self , root ):
        # write code here
        res = []
        def inorder(root):    ###dfs 思想递归
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res

### other way：
### 手写
class Solution:
    def inorderTraversal(self , root ):
        # write code here
        res, stack = [], []
        cur  = root
        while stack or cur:
            if cur :
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
            
### 前中后三序遍历
class Solution:
    def threeOrders(self , root: TreeNode) -> List[List[int]]:
        # write code here
        res = [[],[],[]]
        def dfs(root):
            if not root: return None
            res[0].append(root.val) ## 前： 根左右
            dfs(root.left)
            res[1].append(root.val) ## 中： 左根右
            dfs(root.right)
            res[2].append(root.val) ## 后： 左右根
        dfs(root)
        return res

### leecode 145 后序 
### leetcode 144 前序
### leetcode 94 中序

                
### leetcode 104 二叉树的最大深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        a = max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        return a

### leetcode 101. 对称二叉树
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                return check(p.right, q.left) and check(p.left, q.right)
        return check(root.right, root.left)


###leetcode 98. 验证二叉搜索树
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')) -> bool:
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root)


