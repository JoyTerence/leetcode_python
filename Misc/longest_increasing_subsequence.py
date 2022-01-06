
def quadtratic(nums):

    dp = [1] * len(nums)

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)
    
    return max(dp)

'''
Time: O(N^2)
Space: O(N)
'''

def binary(nums):

    sub = []
    
    for num in nums:
        idx = bisect_left(sub, num)

        if idx == len(sub):
            sub.append(num)
        else:
            sub[idx] = num
    
    return len(sub)

'''
Time: O(N * LogN)
Space: O(1)
'''