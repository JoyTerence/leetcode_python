

def linear_approach(nums, k):

    if k <= arr[0] - 1:
        return k

    s = arr[0] - 1

    for i in range(len(arr)-1):
        diff = arr[i+1] - arr[i] - 1
        if s + diff >= k:
            return arr[i] + k - s
        s += diff

    return arr[-1] + k - s

'''
Time: O(N)
Space: O(1)
'''

def binary_search_approach(nums, k):

    l, r = 0, len(arr)-1

    while l <= r:
        mid = (l+r) // 2
        if arr[mid] - mid - 1 < k:
            l = mid + 1
        else:
            r = mid - 1

    return l + k

'''
Time: O(logN)
Space: O(1)
'''