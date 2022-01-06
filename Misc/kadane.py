
def kadane(nums):

    s, m = nums[0], nums[0]

    for num in nums[1:]:
        s = max(s+num, num)
        m = max(m, s)
    
    return m