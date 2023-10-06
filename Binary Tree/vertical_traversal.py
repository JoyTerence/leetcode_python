from collections import deque, collections

def vertical_traversal(root):

    q = deque()
    q.append((root, 0))

    d = collections.defaultdict(list)

    while q:
        ele, col = q.popleft()
        if ele:
            d[col].append(ele.val)
            if ele.left:
                q.append((ele.left, col-1))
            if ele.right:
                q.append((ele.right, col+1))

    temp_ans = []
    for k in d:
        temp_ans.append((k, d[k]))
    
    temp_ans.sort(key = lambda x: x[0])

    final_ans = []
    for i in temp_ans:
        final_ans.append(i[1])
    
    return final_ans

'''
Time: O(NlogN)
Space: O(N)
'''