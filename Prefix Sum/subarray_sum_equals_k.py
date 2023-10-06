
import collections


def subarray_sum_equals_k(nums, k):
    
    hmap = collections.defaultdict(int)
    hmap[0] = 1
    s, count = 0, 0

    for num in nums:
        s += num

        if s - k in hmap:
            count += hmap[s-k]
        hmap[s] += 1
    
    return count


