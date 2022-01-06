
'''
recover BST with two swapped nodes
'''

def recover_bst(root):

    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    
    def find_two_swapped(nums):
        x = y = -float('inf')
        for i in range(len(nums)-1):
            if nums[i+1] < nums[i]:
                y = nums[i+1]
                if x == -float('inf'):
                    x = nums[i]
                else:
                    break
        return x, y
    
    def recover(root, count):
        if root:
            if root.val == x or root.val == y:
                root.val = y if root.val == x else x
                count -= 1
                if count == 0:
                    return
            recover(root.left, count)
            recover(root.right, count)
    
    nums = inorder(root)
    x, y = find_two_swapped(nums)
    recover(root, 2)

'''
Time: O(N)
Space: O(N)
'''

def recover_bst(root):

    stack = []
    x = y = prev = None

    def iterative(root):
        nonlocal x,y,prev
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if prev and root.val < prev.val:
                y = root
                if not x:
                    x = prev
                else:
                    return
            prev = root
            root = root.right
    
    iterative(root)

    x.val, y.val = y.val, x.val

'''
Time: O(N)
Space: O(N)
'''

