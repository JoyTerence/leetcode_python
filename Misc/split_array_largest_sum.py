
'''
Given an array nums which consists of non-negative integers and an integer m,

you can split the array into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.
'''

def split_array_largest(nums, m):

    l, r = 0, 0

    for num in nums:
        r += num
        if num > l:
            l = num

    ans = r

    while l <= r:
        mid = (l+r) // 2
        sum, count = 0, 1
        for num in nums:
            if sum+num > mid:
                count += 1
                sum = num
            else:
                sum += num
        if count <= m:
            ans = min(ans, mid)
            r = mid - 1
        else:
            l = mid + 1
    
    return ans

'''
Time: O(N*log(total_possible_sums))
Space: O(1)
'''