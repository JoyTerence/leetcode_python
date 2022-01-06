
def minimum_size_subarray_sum(nums, target):

    left = 0
    sum = 0

    min_len = float('inf')

    for right in range(len(nums)):
        sum += nums[right]

        while sum >= target:
            min_len = min(min_len, right - left + 1)
            sum -= nums[left]
            left += 1
    
    return min_len if min_len != float('inf') else 0

'''
Time: O(N)
Space: O(1)
'''