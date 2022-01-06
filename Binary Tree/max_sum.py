
def max_sum(root):

    def recursion(root):
        if not root:
            return 0
        
        left_sum = max(recursion(root.left), 0)
        right_sum = max(recursion(root.right), 0)
        
        not_considering_ancestor = left_sum + right_sum + root.val

        nonlocal ans
        ans = max(ans, not_considering_ancestor)

        # for recursion to send only max value above
        return root.val + max(left_sum, right_sum)

    ans = float('-inf')
    return ans

'''
Time complexity: O(N), where N is number of nodes, since we visit each node not more than 2 times.

Space complexity: O(H), where H is a tree height, to keep the recursion stack. 
In the average case of balanced tree, the tree height H = logN, in the worst case of skewed tree, H = N.
'''