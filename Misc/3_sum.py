
def three_sum(nums):

    res, dups = set(), set()

    n = len(nums)

    for i in range(n):
        if nums[i] not in dups:
            dups.add(nums[i])
            seen = set()
            for j in range(i+1, n):
                comp = -nums[i]-nums[j]
                if comp in seen:
                    res.add(tuple(sorted((nums[i], nums[j], comp))))
                seen.add(nums[j])
    
    return res

'''
Time Complexity: O(N^2).

We have outer and inner loops, each going through N elements.

While the asymptotic complexity is the same, this algorithm is noticeably slower than the previous approach. 

Lookups in a hashset, though requiring a constant time, are expensive compared to the direct memory access.

Space Complexity: O(N) for the hashset/hashmap.
'''