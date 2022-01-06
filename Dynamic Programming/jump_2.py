
# GREEDY
def jumps(nums):
    jumps = currentJumpEnd = farthestReachable = 0
    for i in range(len(nums)-1):
        farthestReachable = max(farthestReachable, i+nums[i])
        if i == currentJumpEnd:
            jumps += 1
            currentJumpEnd = farthestReachable
    return jumps

'''
Time Complexity: O(N) because there are N elements in the array and we visit each element in the array only once.

Space Complexity: O(1) because we don't use any additional data structures.

'''

# DYNAMIC PROGRAMMING
def jumps(nums):
    dp = [float('inf')] * len(nums)
    dp[0] = 0
    for i in range(len(nums)):
        for j in range(i):
            if j+nums[j]>=i:
                dp[i] = min(dp[i], dp[j]+1)
    return dp[-1]

'''
Time Complexity: O(N^2) because there are NN elements in the array and we visit each element in the array only once.

Space Complexity: O(N) because we don't use any additional data structures.

'''