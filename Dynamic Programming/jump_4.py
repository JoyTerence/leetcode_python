
'''

Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

'''

def minJumps(arr):

    n = len(arr)

    graph = {}

    for i in range(n):
        if arr[i] in graph:
            graph[arr[i]].append(i)
        else:
            graph[arr[i]] = i

    curr = [0]
    visited = set([0])
    steps = 0

    # when current layer exists
    while curr:
        next = []

        # iterate the layer
        for node in curr:
            
            # check if reached end
            if node == n-1:
                return steps

            # check same value
            for child in graph[arr[node]]:
                if child not in visited:
                    visited.add(child)
                    next.append(child)
            
            # clear the list to prevent redundant search
            graph[arr[node]].clear()

            # check neighbors
            for child in [node-1, node+1]:
                if 0<=child<len(arr) and child not in visited:
                    visited.add(child)
                    next.append(child)
        
        curr = next
        steps += 1
    
    return -1

'''
Simply BFS traversal

Time complexity: O(N) since we will visit every node at most once.

Space complexity: O(N) since it needs curs and nex to store nodes.
'''
