
def longest_consecutive(nums):

    nums = set(nums)
    m = 0

    for num in nums:
        if num - 1 not in nums:
            curr = num
            length = 1

            while curr+1 in nums:
                curr += 1
                length += 1
            
            m = max(length, m)
    
    return m

'''
Time: O(N)
Space: O(1)
'''